def read_coordinates(filename):

    liste = []

    with open(filename, 'r') as file:
        for lines in file:
            line = lines.strip()
            if line:
                i,j = line.split(",")
                liste.append((float(i), float(j)))
    return liste

