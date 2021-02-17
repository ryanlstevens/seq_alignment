import numpy as np
from itertools import product

class local_similarity_test:
    """
    A class used to compute local similarity

    ...

    Attributes
    ----------
    str1 : str or list of characters
        first string to compare
    str2 : str or list of characters
        second string to compare
    backtrace : bool
        flag for whether to perform backtrace
    edit_array : numpy.array
        array of edit distances
    match_distance : int
        optimal value of similarity problem
    backtrace_array : numpy.array
        3d binary array of backtrace operations. In 3rd dimension, 1st is 
        empty string, 2nd is insertion, 3rd is deletion, 4th is match
    backtrace_path : list
        list of indices showing the optimal backtrace path
    backtrace_table : numpy.array
        array showing the entire backtrace 
    match_alignment_table : numpy.array
        array with aligned strings in first 2 rows. 3rd row is edit actions

    Methods
    -------
    make_edit_array()
        Create edit array, which holds edit distance values
    align_matches()
        Aligns matches
    """

    def __init__(self
                ,str1
                ,str2
                ,backtrace=False
                ,op_costs={'Delete':-1
                          ,'Insert':-1
                          ,'Substitute':-1
                          ,'Exact':2}):
        
        # Set parameter variables
        self.str1 = str1 
        self.str2 = str2
        self.edit_array = None
        self.backtrace = backtrace

        if self.backtrace:
            self.backtrace_array = None
            self.backtrace_path = None
            self.backtrace_table = None
            self.match_alignment_table = None
        
        # Set helper values
        self.len1 = len(self.str1) + 1 # Count empty string
        self.len2 = len(self.str2) + 1 # Count empty string

        # Set values of cost of operations
        self.op_costs = op_costs

        # Maximum string distance must be greater than insert + deleting all
        self.match_distance = self.len1*self.op_costs['Delete'] + \
                              self.len2*self.op_costs['Insert']

    def run(self):
        """Run string distance algorithm to find maximum similarity score b/w strings
         
        Always assumes the string distance is maximum value of the edit distance array


        Methods
        -------
        _run_with_backtrace()
            runs algorithm, storing backtrace values in backtrace_array
        _run_without_backtrace()
            runs algorithm, not storing backtrace values
        _align_matches()
            uses backtrace values to find optimal alignment path, 
            returns alignment of strings and edit actions used to create
            alignment

        Outputs 
        -------
        edit_distance : float
            minimum number of edits to transform str1 into str2
        match_alignment_table : numpy.array (optional)
            array with aligned strings in first 2 rows. 3rd row is edit actions.
            only occrus if backtrace = True. 
        """

        if self.backtrace:
            # Run string matching, keeping edit distance array
            self._run_with_backtrace()

            # Create string alignment from str1 to str2,
            #  with edit distance operations
            self._align_matches()
        
        else:
            # Run string matching, storing edit distance array
            self._run_without_backtrace()


    def _run_with_backtrace(self):
        """Create edit array, which holds edit distance values"""
        
        ## Create initial array to hold edit
        ##  dist values
        ##
        ## Add extra row + column for empty string
        self.edit_array = np.empty((self.len1,self.len2),dtype= np.int8)

        ## Initialize first row + column of array
        ##  for the empty string value
        self.edit_array[:,0] = 0
        self.edit_array[0,:] = 0

        if self.backtrace:
            self.backtrace_array = np.zeros((self.len1,self.len2,4),dtype= bool)

        ## Fill in row by row
        for ii in range(1,self.len1):
            for jj in range(1,self.len2):
            
                # Get last letter from string, and compare value
                sub1 = self.str1[ii-1]
                sub2 = self.str2[jj-1]
                
                # Find maximum values using
                #  bellman recursion
                #
                # Order is : [Zero String, Insert, Delete, Substitute or Exact Match]

                # Value of substitute or exact match
                t_ij = self.op_costs['Substitute']*(sub1!=sub2) + self.op_costs['Exact']*(1-(sub1!=sub2))

                # Values of zero string, inserting, deleting and substituting
                action_values = [0
                                ,self.edit_array[ii,jj-1]+self.op_costs['Insert']
                                ,self.edit_array[ii-1,jj]+self.op_costs['Delete']
                                ,self.edit_array[ii-1,jj-1]+t_ij,
                                ]

                # What is maximum value of action
                max_val = np.max(action_values)
                self.edit_array[ii,jj] = max_val

                # Keep track of global maximum 
                if max_val > self.match_distance:
                    self.match_distance = max_val

                if self.backtrace:
                    self.backtrace_array[ii,jj,np.where(action_values==max_val)] = 1
        
    
    def _run_without_backtrace(self):
        """Create edit array, which holds edit distance values"""


        ## Initialize first row of array + first element of next row
        ##  for the empty string value
        past_row = [0]*self.len2
        curr_row_num = 1
        curr_row = [0]

        ## Index for str2 to iterate over
        col_idx = np.arange(1,self.len2)

        ## Go row by row, keeping track of past row + current row only
        while curr_row_num < self.len1:
            # Define append function only once for speed-up
            curr_row_append = curr_row.append
            for col_num in col_idx:
                # Get substrings to compare
                last_ltr_1 = self.str1[curr_row_num-1]
                last_ltr_2 = self.str2[col_num-1]

                # Find maximum values using
                #  bellman recursion
                #
                # Order is : [Insert, Delete, Substitute or Exact Match]

                # Value of substitute or exact match
                t_ij = self.op_costs['Substitute']*(last_ltr_1!=last_ltr_2) + self.op_costs['Exact']*(1-(last_ltr_1!=last_ltr_2))

                # Values of inserting, deleting and substituting
                max_val = max(
                            [
                            0
                            ,curr_row[col_num-1]+self.op_costs['Insert']
                            ,past_row[col_num]+self.op_costs['Delete']
                            ,past_row[col_num-1]+t_ij
                            ]
                            )
                curr_row_append(max_val)

                # Keep track of global maximum 
                if max_val > self.match_distance:
                    self.match_distance = max_val

                
            # Moving onto to comparing next letter in the first string 
            # i.e. moving down a row
            curr_row_num+=1
            past_row = curr_row 
            curr_row = [0]
        
    def _get_shortest_path(self):
        '''Gets the shortest path through edit array

        Requires backtrace array, set backtrace = True when 
          initializing class
        '''
        ## Start at max value of edit array
        i, j = np.unravel_index(np.argmax(self.edit_array),self.edit_array.shape)
        self.match_distance = self.edit_array[i,j]

        self.backtrace_path = [(i,j)]

        while (i,j) != (0,0):
            # Empty
            if self.backtrace_array[i,j,0]==1:
                break
            # Insertion
            if self.backtrace_array[i,j,1]==1:
                i,j = (i,j-1)
            # Deletion
            elif self.backtrace_array[i,j,2]==1:
                i,j = (i-1,j)
            # Substitution/Exact Match
            elif self.backtrace_array[i,j,3]==1:
                i,j = (i-1,j-1)
            self.backtrace_path.append((i,j))

    def _align_matches(self):
        '''Align matches

        Requires backtrace array, set backtrace = True when 
          initializing class
        '''
        # Get shortest path
        self._get_shortest_path()
        
        # Initialize aligned text
        str1_aligned = []
        str2_aligned = []
        action = []

        for ix in range(len(self.backtrace_path)-1,0,-1):
            i_0, j_0 = self.backtrace_path[ix]
            i_1, j_1 = self.backtrace_path[ix-1]

            # Replacement/Substitution
            if i_1 > i_0 and j_1 > j_0:
                # Do letters match 
                if self.str1[i_1-1]==self.str2[j_1-1]:
                    action.append('S')
                else:
                    action.append('R')
                str1_aligned.append(self.str1[i_1-1])
                str2_aligned.append(self.str2[j_1-1])
            # Insertion
            elif i_1==i_0:
                action.append('I')
                str1_aligned.append(' ')
                str2_aligned.append(self.str2[j_1-1])
            # Deletion 
            elif j_1==j_0:
                action.append('D')
                str1_aligned.append(self.str1[i_1-1])
                str2_aligned.append(' ')

        self.match_alignment_table = np.array([str1_aligned,str2_aligned,action])


    