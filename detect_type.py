def detect_type(L):
    for i in range(len(L)):                                                     # every sublist of L                                            
        for j in range(len(L[i])):                                                   # for j spanning indices of x
             if isinstance(L[i][j], (str, list, dict, tuple)) == True:             # checks if any of the elements                
                 return False, 'nonvalid data object type'                                          # cannot use it as a matrix
    return True, 'valid'
