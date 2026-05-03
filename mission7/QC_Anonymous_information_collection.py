def collect(data):
    try:
        dictionary = {}
        with open(data, 'r') as file:
            for lines in file:
                lines = lines.strip()
                if not lines:
                    continue
                nature = extract(lines)
                pattern = treatment(nature)
                if pattern in dictionary:
                    dictionary[pattern] += 1
                else:
                    dictionary[pattern] = 1
                
        return dictionary
    
    except Exception as e:
        print(f"Une erreur est survenu : {e}")
        return e