def list_difference(numlist1, numlist2):
    '''
    Purpose:
        Find the difference between the numbers in a list
    Parameters:
        numlist1: a list containing integers
        numlist2: a list containing integers that is subtracting from numlist1
    Return Values:
        A new list that contains the difference between the two lists
    '''
    difference = [numlist1[i]-numlist2[i] for i in range(len(numlist1))]
    return difference

def larger_decrement(numlist, n):
    '''
    Purpose:
        Determine if there are any integers in the given list are larger than 'n'
    Parameters:
        numlist: a list containing integers, which may include the same integer twice
        n: an integer used, to see if the list contains any numbers larger than 'n'
    Return Values:
       Return boolean operator True or False, depending if the given has any values larger than 'n'
    '''
    found = False
    max_num = float('-inf')
    max_index = -1
    for i in range(len(numlist)):
        if numlist[i] > n:
            found = True
            if numlist[i] > max_num:
                max_num = numlist[i]
                max_index = i
    if found:
        numlist[max_index] -= 1
        return True
    else:
        return False
    
def word_mix(wordlist1, wordlist2):
    '''
    Purpose:
        Combine two word lists and alternate, the words between the two starting with wordlist1
    Parameters:
        wordlist1: list containing strings
        wordlist2: list containing strings
    Return Value:
        A string that is a combination of the two word lists, which alternates between wordlist1 and wordlist2
    '''
    i = 0
    j = 0
    mixed = []
    while i < len(wordlist1) and j < len(wordlist2):
        if i <= j:
            mixed.append(wordlist1[i])
            i += 1
        else:
            mixed.append(wordlist2[j])
            j += 1
    while i < len(wordlist1):
        mixed.append(wordlist1[i])
        i += 1
    while j < len(wordlist2):
        mixed.append(wordlist2[j])
        j += 1
    return " ".join(mixed)

