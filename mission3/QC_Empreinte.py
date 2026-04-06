def empreinte_carbone(distance):
 
    if distance <= 1500:
        RF = 2.0
    else:
        RF = 2.7
        
    x = (distance * 0.25) * RF

    if x <= 200:
        return 'faible'
    elif 200 < x <= 1200:
        return 'modéré'
    elif 1200 < x <= 4000:
        return 'élevé'
    elif 4000 < x:
        return "très élevé"
print(empreinte_carbone(1400))
print(empreinte_carbone(0))
print(empreinte_carbone(3000))
print(empreinte_carbone(1500))
