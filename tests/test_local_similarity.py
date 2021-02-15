def local_similarity_setup():

    # ~~~ Local Similarity ~~~ #

    from src.local_similarity import main as local_similarity

    str1 = ['p','q','r','a','x','a','b','c','s','t','v','q']
    str2 = ['x','y','a','x','b','a','c','s','l','l']            

    # Initalize matching class function
    ls_init = local_similarity.local_similarity(str1,str2,True)

    # Run matching 
    ls_init.make_edit_array()   

    return ls_init


def test_local_similarity_alignment():
    
    import numpy as np

    ls_init = local_similarity_setup()

    ls_init.align_matches()
    alignment = np.array(ls_init.match_alignment_table)

    correct_answer = np.array([['a', 'x', 'a', 'b', ' ', 'c', 's'],
                               ['a', 'x', ' ', 'b', 'a', 'c', 's'],
                               ['S', 'S', 'D', 'S', 'I', 'S', 'S']])
    
    assert np.array_equal(alignment, correct_answer)