import csv 
import os

# ~~~ Read in testing data ~~~ #
def create_test_data(path_to_data):
    alignment_tests=[]
    with open(path_to_data) as ifile:
        reader = csv.reader(ifile)
        for r in reader:
            alignment_tests.append((r[0],r[1]))
        
    alignment_tests = alignment_tests[:10]
    
    return(alignment_tests)


# ~~~ Create timing function ~~~ #
def run_matching(run_function,test_data,backtrace=False):
    ix=0
    for elems in test_data:
        ix+=1
        # Initalize matching class function
        wf_init = run_function(elems[0],elems[1],backtrace)
        # Run matching 
        wf_init.run() 
