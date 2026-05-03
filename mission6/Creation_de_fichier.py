def write_a(filename, n):
    with open(filename, 'w') as file:
        char = 'a' * n
        file.write(char)