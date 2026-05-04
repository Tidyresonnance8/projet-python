class Student:
    def __init__(self, firstname, surname, mark):
        """
        @pre:  firstname et surname sont des str et mark est un int
        @post: crée une instance de Student avec ces trois attributs
        """
        self.firstname = firstname
        self.surname = surname
        self.mark = mark

    def marks_from_file(filename):
        liste = []
        with open(filename, 'r') as file:
            for lines in file:
                line = lines.strip().split()
                if not line:
                    continue
                if len(line) != 3:
                    continue
                if line:
                    liste.append(Student(line[0], line[1], int(line[2])))
        return liste