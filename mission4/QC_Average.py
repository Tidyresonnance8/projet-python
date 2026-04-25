def average(lst):
    if len(lst) == 0:
        return None
    
    longueur = len(lst)
    total = 0
    
    for element in lst:
        total += element
        average = total/longueur

    return average

