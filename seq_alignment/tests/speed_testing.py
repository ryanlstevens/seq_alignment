# Colors for printing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Add Parent Directory to Python Path (HACK: DON"T PUT IN PRODUCTION)
import os 
import inspect 
import sys 
import timeit 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Get path to data files
path_to_data = os.path.join(parentdir,'data/seq_alignments/seq_alignment.csv')

# PYTHON RELOAD THE SOURCE FILE
os.chdir('../')
print(os.getcwd())
from seq_alignment.wagner_fisher.main import wagner_fisher as wf_curr
from seq_alignment.wagner_fisher.main_test import wagner_fisher as wf_new
from seq_alignment.helpers.speed_test import create_test_data, run_matching
from functools import partial 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~ RUN SPEED IMPROVEMENT TEST ~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# PARAMETERS
SPEED_IMPROVEMENT_THRESHOLD = 2   #<- Speed improvement > than this, then test is a success

# Create test data #
test_data = create_test_data(path_to_data)

# Run speed test on old code + new code #
curr_version = timeit.Timer(partial(run_matching,run_function=wf_curr,test_data=test_data,backtrace=False))
new_version = timeit.Timer(partial(run_matching,run_function=wf_new,test_data=test_data,backtrace=False))
curr_version_run = curr_version.timeit(2)
new_version_run = new_version.timeit(2)

# Create variables indicating whether there was a speed improvement
#  and change color of message to green if there is and red if there is no
run_time_change = curr_version_run/new_version_run
speed_test_outcome = run_time_change>SPEED_IMPROVEMENT_THRESHOLD
outcome_color = bcolors.OKGREEN if speed_test_outcome else bcolors.FAIL 
outcome_message = 'SUCCESSFUL SPEED IMPROVEMENT' if speed_test_outcome else 'NO SPEED IMPROVEMENT' 

# Return improvement
print('{color_start}{outcome_message}{color_end} : New code improves Old code by {color_start}{run_time_change:2.2f}x{color_end}'.format(color_start=outcome_color
                                                                                                 ,color_end=bcolors.ENDC
                                                                                                 ,outcome_message=outcome_message
                                                                                                 ,run_time_change=run_time_change))