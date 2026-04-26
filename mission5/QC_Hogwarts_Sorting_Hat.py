knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
        ['Ravenclaw', ['smart', 'wise', 'curious']],
        ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
        ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    g,r,h,s = 0,0,0,0

    for qualities in student_qualities:
        if qualities in knowledge[0][1]:
            g += 1
        if qualities in knowledge[1][1]:
            r += 1
        if qualities in knowledge[2][1]:
            h += 1
        if qualities in knowledge[3][1]:
            s += 1
        
    resultat = [['Gryffindor', g], ['Ravenclaw', r], ['Hufflepuff', h], ['Slytherin', s]]
    tri_maison = []

    while len(resultat) != 0:

        max_score = -1
        max_maison = None
        max_index = 0
        i = 0

        for maison, score in resultat:
            if max_score < score:
                max_score = score
                max_maison = maison
                max_index = i
            i += 1
        tri_maison.append(max_maison)
        resultat.pop(max_index)

    return tri_maison