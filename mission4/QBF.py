def positions(p,s):
    """
    pre : p est un pattern, c'est-à-dire une chaîne de
        caractères qui peut contenir des lettres, des chiffres et le caractère '?'
        s contient des lettres et des chiffres mais pas le caractère '?'
    post : retourne une liste des occurrences du pattern p à l'intérieur
        de la chaîne de caractères s. Une occurrence est une sous-chaîne de s
        de même longueur que p qui contient les mêmes caractères que p à
        toutes les positions, '?' peut remplacer tous les caractères.
        en ignorant les majuscules et minuscules
    """
    occurences = []
    p = p.lower()
    s = s.lower()

    for i in range(len(s)-len(p)+1):             # nous allons déplacer notre motif p au-dessus de la chaîne s
        match = True
        for j in range(len(p)):
            if "?" != p[j] and p[j] != s[i+j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences
print(positions("ab","CDEF"))
print(positions("?B","CAbDEF"))
print(positions("A?","CABDEACF"))
print(positions("aa","CAAABDEAAF"))
print(positions("??","CAAAB"))