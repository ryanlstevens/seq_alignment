# Change directory 
import os 

import numpy as np

os.chdir("C:/Users/jmcgn/Desktop/py_string_matchers/") #<- CHANGE TO PATH WHERE ROOT OF THIS FOLDER LIVES

# ~~~ Wagner Fischer ~~~ #
from src.wagner_fisher import main as wagner_fischer

# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
wagner_fischer_init = wagner_fischer.wagner_fischer(str1,str2,True)

# Run matching 
wagner_fischer_init.run()

# Get alignment 
wagner_fischer_init.align_matches()
print('ALIGNMENT TABLE')
print(np.array(wagner_fischer_init.match_alignment_table))

# Make backtrace table 
print('\nBACKTRACE DIRECTIONS')
print(np.array(wagner_fischer_init.make_backtrace_table())) 
