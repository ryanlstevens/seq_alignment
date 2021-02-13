def wagner_fisher_setup():

    # ~~~ Wagner Fischer ~~~ #
    from src.wagner_fisher import main as wagner_fischer

    str1=['v','i','n','e']
    str2=['v','i','n']  

    # Initalize matching class function
    wagner_fischer_init = wagner_fischer.wagner_fischer(str1,str2,True)

    # Run matching 
    wagner_fischer_init.run()   

    return wagner_fischer_init



def test_wagner_fisher_alignment():
    
    import numpy as np

    wagner_fischer_init = wagner_fisher_setup()

    wagner_fischer_init.align_matches()
    alignment = np.array(wagner_fischer_init.match_alignment_table)

    correct_answer = np.array([['v', 'i', 'n', 'e'], 
                               ['v', 'i', 'n', ' '], 
                               ['S', 'S', 'S', 'D']])
    
    assert np.array_equal(alignment, correct_answer)



def test_wagner_fisher_backtrace():
    
    import numpy as np

    wagner_fischer_init = wagner_fisher_setup() 

    # Get alignment 
    wagner_fischer_init.make_backtrace_table()
    backtrace_table = np.array(wagner_fischer_init.make_backtrace_table())

    correct_answer = np.array([['⇐', '⇐', '⇐', '⇐'],
                              ['⇑', '⇖', '⇐', '⇐'],
                              ['⇑', '⇑', '⇖', '⇐'],
                              ['⇑', '⇑', '⇑', '⇖'],
                              ['⇑', '⇑', '⇑', '⇑']])
    
    assert np.array_equal(backtrace_table, correct_answer)
