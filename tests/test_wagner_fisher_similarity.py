def wagner_fisher_setup(backtrace=True):

    # ~~~ Wagner Fischer ~~~ #
    from src.wagner_fisher_similarity import main as wagner_fisher_similarity

    str1=['v','i','n','e']
    str2=['v','i','n']  

    # Initalize matching class function
    wf_init = wagner_fisher_similarity.wagner_fisher_similarity(str1,str2,backtrace)

    # Run matching 
    wf_init.run()   

    return wf_init



def test_wagner_fisher_alignment():
    
    import numpy as np

    wf_init = wagner_fisher_setup()

    wf_init.run()
    alignment = np.array(wf_init.match_alignment_table)

    correct_answer = np.array([['v', 'i', 'n', 'e'], 
                               ['v', 'i', 'n', ' '], 
                               ['S', 'S', 'S', 'D']])
    
    assert np.array_equal(alignment, correct_answer)



def test_wagner_fisher_backtrace():
    
    import numpy as np

    wf_init = wagner_fisher_setup() 

    # Run matching
    wf_init.run()

    # Get alignment 
    wf_init.make_backtrace_table()
    backtrace_table = np.array(wf_init.backtrace_table)

    correct_answer = np.array([['⇐', '⇐', '⇐', '⇐'],
                              ['⇑', '⇖', '⇐', '⇐'],
                              ['⇑', '⇑', '⇖', '⇐'],
                              ['⇑', '⇑', '⇑', '⇖'],
                              ['⇑', '⇑', '⇑', '⇑']])
    
    assert np.array_equal(backtrace_table, correct_answer)

def test_backtrace_result_same():
    
    import numpy as np 

    # Initialize two classes, one with backtrace 
    #  and one without backtrace
    wf_backtrace = wagner_fisher_setup(True)
    wf_no_backtrace = wagner_fisher_setup(False)

    # Run string distance 
    wf_backtrace.run()
    wf_no_backtrace.run()

    # Compare that answers are the same
    assert np.array_equal(wf_backtrace.match_distance,wf_no_backtrace.match_distance)
