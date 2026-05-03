def write_coordinates(filename, l):
    with open(filename, 'w') as file:
        for x, y in l:
            file.write(f"{x},{y}\n")
             