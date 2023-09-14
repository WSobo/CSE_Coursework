# author:Will Sobolewski (1846541)


def make_dict(words: list):
    '''
    input: a list of strings

    returns: a dictionary where keys are integers from 1 to 10 and values are lists composed of strings of the same length and accessed by the key that is equal to the length of strings in the list.
    If a string has the length greater than 10, it should be placed in the list with the key equal to 10. The input of the function is a list of strings.
    '''
    dictionary = {}
    for word in words:
        length = len(word)
        if length > 10:
            length = 10
        if length not in dictionary:
            dictionary[length] = []
        dictionary[length].append(word)
    return dictionary


if __name__ == '__main__':

    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(
        ['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print(dictionary)
    assert dictionary == d
    print('Everything works correctly!')
