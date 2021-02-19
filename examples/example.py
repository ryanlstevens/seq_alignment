# Change directory 
import numpy as np

# ----------------------
# GLOBAL ALIGNMENT RUNS
# ----------------------

## Run algo getting both edit distance +
##  backtrace table

from seq_alignment import global_similarity

# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
sim_init = global_similarity(str1,str2,True)

# Run matching 
sim_init.run()

# Get edit distance
print("EDIT DISTANCE")
print(sim_init.match_distance)

# Get alignment 
print('\nALIGNMENT TABLE')
print(np.array(sim_init.match_alignment_table))

# Make backtrace table 
print('\nBACKTRACE DIRECTIONS')
print(np.array(sim_init.make_backtrace_table())) 


## Run algo getting ONLY edit distance 
## 
## This runs faster due to not having to store
## backtrace values

from seq_alignment import global_similarity

# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
sim_init = global_similarity(str1,str2,False)

# Run matching 
sim_init.run()

# Get edit distance
print("EDIT DISTANCE")
print(sim_init.match_distance)

# ----------------------
# LOCAL ALIGNMENT RUNS
# ----------------------

## Run algo getting both edit distance +
##  backtrace table

from seq_alignment import local_similarity

# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
sim_init = local_similarity(str1,str2,True)

# Run matching 
sim_init.run()

# Get edit distance
print("EDIT DISTANCE")
print(sim_init.match_distance)

# Get alignment 
print('\nALIGNMENT TABLE')
print(np.array(sim_init.match_alignment_table))

# Make backtrace table 
print('\nBACKTRACE DIRECTIONS')
print(np.array(sim_init.make_backtrace_table())) 
