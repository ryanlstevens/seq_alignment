# Description

Module to determine distances between two strings (or two lists of strings). The primary use case of this package is to allow users to both compute distance measures using different distance algorithms. Additionally, we provide additional functionality to both visualize the alignment of the two strings. This allows users to determine how one string is transformed into another.

# Algorithms Available

## Wagner Fischer

```python
# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
wagner_fischer_init = wagner_fischer(str1,str2,True)

# Run matching 
wagner_fischer_init.run_matching()

# Get alignment 
wagner_fischer_init.align_matches()
print('ALIGNMENT TABLE')
print(np.array(wagner_fischer_init.match_alignment_table))

# Make backtrace table 
print('\nBACKTRACE DIRECTIONS')
wagner_fischer_init.make_backtrace_table()
```
