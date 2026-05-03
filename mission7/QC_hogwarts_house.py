def winning_house(scroll):
    house_score = {'gryffindor' : 0, 'ravenclaw' : 0, 'hufflepuff' : 0, 'slytherin' : 0}
    student_to_house = {}
    for house, student_list in students.items():
        for student in student_list:
            student_to_house[student.strip()] = house
    with open(scroll,'r') as file:
        for lines in file:
            line = lines.strip()
            if not line:
                continue
            element = line.split()
            if len(element) != 2:
                continue
            name = element[0]
            try:
                points = int(element[1])
            except ValueError:
                continue
            if name in student_to_house:
                house = student_to_house[name]
                house_score[house] += points
    max_score = max(house_score.values())
    winners = []
    for house, score in house_score.items():
        if score == max_score:
            winners.append(house)
    if len(winners) == 1:
        return winners[0]
    else:
        return winners