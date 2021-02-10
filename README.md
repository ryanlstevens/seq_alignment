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

# For us

## Module convention 

Each algorithm should have the following methods :

* __init__ : accepts string or list, and optional argument defining if user should get backtrace table
* run : runs matching algorithm
* align_matches : aligns strings 
* make_backtrace_table : constructs backtrace directions 

## Random stuff

Python style guide : https://www.python.org/dev/peps/pep-0008/

__KEY POINTS__

__GENERAL__    
__4 space indention__    
__Limit lines to 80 characters__   
__No hanging indents for multi-line functions (this pep allows them, but I don't like them):__

```python

# Aligned with opening delimiter
foo = long_func(var_one
               ,var_two)

# Hanging indent (I don't like)
foo = long_func(
    var_one
   ,var_two)
```

__FUNCTIONS AND CLASSES__   
__Top-level functions + classes surrounded by 2 blank lines__  
__Methods inside classes surround by 1 blank line__   
__Explicitly define input type in functions__  

```python
# Correct
def func(input : AnyStr)

# Not as good
def func(input)
```

__IMPORTS__   
__Imports should be one per line__  

``` python
# Correct
import os
import sys

# Incorrect
import os, sys

# Allowed, if from same library
from os import list, join
``` 
__Import order : Standard libraries, related third party, local app specific__  


__NAMES__  
__Package and Modules : short, all-lowercase names__   
__Classes : camel case__     
__Errors : camel case, precede each error with name 'Error'__     
__Functions, Variable Names : lowercase, seperated by underscores__   
__Constants : all capitalized seperated by underscores__   

