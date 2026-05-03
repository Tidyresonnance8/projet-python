def char_count(filename):
    count = 0
    
    with open(filename, 'r') as file:
    
        for line in file:
            for word in line:
                count += 1

    return count
