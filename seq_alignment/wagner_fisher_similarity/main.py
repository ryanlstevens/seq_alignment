import numpy as np
from itertools import product

class wagner_fisher_similarity:
    '''
    Uses wagner-fischer algorithm to compute similarity score 
      between two strings. Additionally, users can output 
      backtrace tables created to run similarity score algorithm.
    '''

    def __init__(self
                ,str1
                ,str2
                ,backtrace=False):
        '''
        INPUT
        ------
        str1 : str or list of strings
        str2 : str or list of strings
        backtrace : boolean
           When set to True, backtrace table is assigned to 
           class parameter `backtrace_array` 
          
        '''
        
        # Set parameter variables
        self.str1 = str1 
        self.str2 = str2
        self.backtrace = backtrace
        self.edit_array = None
        self.match_distance = None
        self.backtrace_array = None
        self.backtrace_path = None
        self.backtrace_table = None
        self.match_alignment_table = None
        
        # Set helper values
        self.len1 = len(self.str1) + 1 # Count empty string
        self.len2 = len(self.str2) + 1 # Count empty string

        # Set values of cost of operations
        self.op_costs = {}
        self.op_costs['Delete'] = -1
        self.op_costs['Insert'] = -1
        self.op_costs['Substitute'] = -2
        self.op_costs['Exact'] = 0

    def run(self):
        '''
        Run string distance algorithm, assumes the string distance 
          can be found in the last row/column of the distance array.
        
        OUTPUT
        ------
        str1 : str or list of strings
        str2 : str or list of strings
        backtrace : boolean
           When set to True, backtrace table is assigned to 
           class parameter `backtrace_array` 
          
        '''

        ## Create initial array to hold edit
        ##  dist values
        ##
        ## Add extra row + column for empty string
        self.edit_array = np.empty((self.len1,self.len2))

        ## Initialize first row + column of array
        ##  for the empty string value
        self.edit_array[:,0] = [i*self.op_costs['Delete'] for i in np.arange(0,self.len1)]
        self.edit_array[0,:] = [i*self.op_costs['Insert'] for i in np.arange(0,self.len2)]

        ## Initalize matrix for backtrace values
        if self.backtrace:
            self.backtrace_array = np.zeros((self.len1,self.len2,3))

        ## Fill in row by row, keeping 
        ##   track of backtrace values 
        for row, col in product(range(1,self.len1),range(1,self.len2)):
            
            # Get substrings to compare
            sub1 = self.str1[row-1]
            sub2 = self.str2[col-1]
            
            # Find minimum values using
            #  bellman recursion
            #
            # Order is : [Insert, Delete, Substitute or Exact Match]

            # Value of substitute or exact match
            t_ij = self.op_costs['Substitute']*(sub1!=sub2) + self.op_costs['Exact']*(1-(sub1!=sub2))

            # Values of inserting, deleting and substituting
            action_values = [self.edit_array[row,col-1]+self.op_costs['Insert']
                            ,self.edit_array[row-1,col]+self.op_costs['Delete']
                            ,self.edit_array[row-1,col-1]+t_ij]

            # What is minimum value of action
            max_val = np.max(action_values)
            self.edit_array[row,col] = max_val
            
            # Which action resulted in minimum value
            if self.backtrace:
                self.backtrace_array[row,col,np.where(action_values==max_val)] = 1

        # Once hit the first col/row can only do deletions/insertions
        if self.backtrace:
            self.backtrace_array[:,0,:] = 0 
            self.backtrace_array[:,0,1] = 1 
            self.backtrace_array[0,:,0] = 1
            self.backtrace_array[0,:,1:] = 0
            
        # Get distance between strings
        self.match_distance = self.edit_array[-1,-1]

        # Return distance between strings
        return(self.match_distance)
    
    def _get_shortest_path(self):
        '''
        Requires backtrace array, set backtrace = True when 
          initializing class
        '''

        ## Start at last element of array
        i, j = self.len1-1, self.len2-1
        self.backtrace_path = [(i,j)]

        while (i,j) != (0,0):
            # Substitution/Exact Match
            if self.backtrace_array[i,j,2]==1:
                i,j = (i-1,j-1)
            # Deletion
            elif self.backtrace_array[i,j,1]==1:
                i,j = (i-1,j)
            # Insertion
            elif self.backtrace_array[i,j,0]==1:
                i,j = (i,j-1)
            self.backtrace_path.append((i,j))

    def make_backtrace_table(self):
        '''
        Requires backtrace array, set backtrace = True when 
          initializing class
        '''

        # Initialize list to hold arrows
        # Index is [row][col]
        self.backtrace_table = []

        # Get total # cols and rows
        rows = self.backtrace_array.shape[0]
        cols = self.backtrace_array.shape[1]

        # Loop through row and col to get direction
        for i in range(0,rows):
            row_elems = []
            for j in range(0,cols):
                directions=''
                btrace_elems = self.backtrace_array[i,j,:]
                if btrace_elems[0]==1:
                    directions=directions+'⇐'
                if btrace_elems[1]==1:
                    directions=directions+'⇑'
                if btrace_elems[2]==1:
                    directions=directions+'⇖'
                row_elems.append(directions)
            self.backtrace_table.append(row_elems)
        
        return(self.backtrace_table)
    
    def align_matches(self):
        '''
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