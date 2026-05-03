def create_index(list_of_words):
    dictionary = {}

    for index, element in enumerate(list_of_words):
        if element in dictionary:
            dictionary[element].append(index)
        else:
            dictionary[element] = [index]
    
    return dictionary
