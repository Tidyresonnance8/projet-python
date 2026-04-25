def extract(code):
    info = ""
    voyelle = "aeiouy"
    voyelle_up = voyelle.upper()
    consonne = "zrtpqsdfghjklmwxcvbn"
    consonne_up = consonne.upper()

    for element in code:
        if element.isdigit():
            info += "number "
        if element.isalpha():
            if element in voyelle:
                info += "vowel-low "
            elif element in voyelle_up:
                info += "vowel-up "
            elif element in consonne:
                info += "consonant-low "
            elif element in consonne_up:
                info += "consonant-up "
    
    return info.strip()

print(extract('AeB7'))
print(extract('65AeBc7'))
