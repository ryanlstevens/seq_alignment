import numpy as np

def local_similarity_setup(str1,str2):

    # ~~~ Local Similarity ~~~ #

    from seq_alignment import local_similarity      

    # Initalize matching class function
    ls_init = local_similarity(str1,str2,True)

    # Run matching 
    ls_init.run()   

    alignment = np.array(ls_init.match_alignment_table)

    return alignment


def test1():

    str1 = ['p','q','r','a','x','a','b','c','s','t','v','q']
    str2 = ['x','y','a','x','b','a','c','s','l','l']    

    correct_answer = np.array([['a', 'x', 'a', 'b', ' ', 'c', 's'],
                               ['a', 'x', ' ', 'b', 'a', 'c', 's'],
                               ['S', 'S', 'D', 'S', 'I', 'S', 'S']])

    alignment = local_similarity_setup(str1,str2)

    assert np.array_equal(alignment, correct_answer)