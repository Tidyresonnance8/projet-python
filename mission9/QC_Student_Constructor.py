class Student:
    __noma = 0
    def __init__(self,firstname,surname,birthday,email):
        self.firstname = firstname
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.noma = Student.__noma
        Student.__noma += 1
    def __str__(self):
        return "L'étudiant numéro {} : {} {} né le {}, peut être contacté par {}".format(self.noma,self.firstname,self.surname,self.birthday,self.email)