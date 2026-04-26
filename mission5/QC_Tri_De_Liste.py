a_list = ...  # liste à trier
sorted_list = ...  # enregistrez dans cette variable la version triée de la liste

temp = a_list[:]
sorted_list = []
while temp != []:
    minimum = temp[0]
    min_index = 0
    i = 0
    while i < len(temp):
        if temp[i] < minimum:
            minimum = temp[i]
            min_index = i
        i += 1
    sorted_list.append(minimum)
    temp.pop(min_index)