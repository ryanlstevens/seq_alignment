def wagner_fisher_setup():

    # ~~~ Wagner Fischer ~~~ #
    from src.wagner_fisher_similarity import main as wagner_fisher_similarity

    str1=['v','i','n','e']
    str2=['v','i','n']  

    # Initalize matching class function
    wf_init = wagner_fisher_similarity.wagner_fisher_similarity(str1,str2,True)

    # Run matching 
    wf_init.run()   

    return wf_init



def test_wagner_fisher_alignment():
    
    import numpy as np

    wf_init = wagner_fisher_setup()

    wf_init.align_matches()
    alignment = np.array(wf_init.match_alignment_table)

    correct_answer = np.array([['v', 'i', 'n', 'e'], 
                               ['v', 'i', 'n', ' '], 
                               ['S', 'S', 'S', 'D']])
    
    assert np.array_equal(alignment, correct_answer)



def test_wagner_fisher_backtrace():
    
    import numpy as np

    wf_init = wagner_fisher_setup() 

    # Get alignment 
    wf_init.make_backtrace_table()
    backtrace_table = np.array(wf_init.make_backtrace_table())

    correct_answer = np.array([['⇐', '⇐', '⇐', '⇐'],
                              ['⇑', '⇖', '⇐', '⇐'],
                              ['⇑', '⇑', '⇖', '⇐'],
                              ['⇑', '⇑', '⇑', '⇖'],
                              ['⇑', '⇑', '⇑', '⇑']])
    
    assert np.array_equal(backtrace_table, correct_answer)
