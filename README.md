# Description [![Build Status](https://travis-ci.com/ryanlstevens/py_string_matchers.svg?token=x6iEoqTBFHFvu6oqChJH&branch=main)](https://travis-ci.com/ryanlstevens/py_string_matchers)

Module to determine distances between two strings (or two lists of strings). The primary use case of this package is to allow users to both compute distance measures using different distance algorithms. Additionally, we provide additional functionality to both visualize the alignment of the two strings. This allows users to determine how one string is transformed into another.

For reference on differences between global and local alignment, see Chapter 11 and 12 of [Algorithms on Strings, Trees, and Sequences](https://www.amazon.com/Algorithms-Strings-Trees-Sequences-Computational/dp/0521585198).

# Algorithms Available

## Global Alignment (Wagner Fischer)

To run the matching, you import `global_similarity` class, initialize with the strings you want to compare (accepts strings or list of strings), and then run your algorithm.

The main options available are whether to compute back-trace, to not compute backtrace and return on edit distance (or string similarity) values set `backtrace = False` when initalizing the class.

```python
## Run algo getting ONLY edit distance 
## 
## This runs fast due to not having to store
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
```

## Local Alignment (Smith Waterman)

Same syntax to running global alignment, but now you import the `local_similarity` class.

```python
## Run algo getting ONLY edit distance 
## 
## This runs fast due to not having to store
## backtrace values

from seq_alignment import local_similarity

# Test values
str1=['v','i','n','e']
str2=['v','i','n']

# Initalize matching class function
sim_init = local_similarity(str1,str2,False)

# Run matching 
sim_init.run()

# Get edit distance
print("EDIT DISTANCE")
print(sim_init.match_distance)
```
