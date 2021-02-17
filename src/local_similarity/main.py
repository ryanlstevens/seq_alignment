import numpy as np
from itertools import product

class local_similarity:

    def __init__(self
                ,str1
                ,str2
                ,backtrace=False):
        
        # Set parameter variables
        self.str1 = str1 
        self.str2 = str2
        self.edit_array = None
        self.match_distance = None
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
        self.op_costs = {}
        self.op_costs['Delete'] = -1
        self.op_costs['Insert'] = -1
        self.op_costs['Substitute'] = -1
        self.op_costs['Exact'] = 2

    def make_edit_array(self):

        ## Create initial array to hold edit
        ##  dist values
        ##
        ## Add extra row + column for empty string
        self.edit_array = np.empty((self.len1,self.len2), dtype=np.int8)

        ## Initialize first row + column of array
        ##  for the empty string value
        self.edit_array[:,0] = 0
        self.edit_array[0,:] = 0

        if self.backtrace:
            self.backtrace_array = np.zeros((self.len1,self.len2,4), dtype=bool)

        ## Fill in row by row
        for row, col in product(range(1,self.len1),range(1,self.len2)):
            
            # Get substrings to compare
            sub1 = self.str1[row-1]
            sub2 = self.str2[col-1]
            
            # Find minimum values using
            #  bellman recursion
            #
            # Order is : [Zero String, Insert, Delete, Substitute or Exact Match]

            # Value of substitute or exact match
            t_ij = self.op_costs['Substitute']*(sub1!=sub2) + self.op_costs['Exact']*(1-(sub1!=sub2))

            # Values of zero string, inserting, deleting and substituting
            action_values = [0
                            ,self.edit_array[row,col-1]+self.op_costs['Insert']
                            ,self.edit_array[row-1,col]+self.op_costs['Delete']
                            ,self.edit_array[row-1,col-1]+t_ij,
                            ]

            # What is minimum value of action
            max_val = np.max(action_values)
            self.edit_array[row,col] = max_val

            if self.backtrace:
                self.backtrace_array[row,col,np.where(action_values==max_val)] = 1

        self.match_distance = self.edit_array[-1,-1]
    
    def _get_shortest_path(self):
        '''
        Requires backtrace array, set backtrace = True when 
          initializing class
        '''
        ## Start at max value of edit array

        i, j = np.unravel_index(np.argmax(self.edit_array),self.edit_array.shape)
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