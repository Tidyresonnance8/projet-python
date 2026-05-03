def save_data(filename, life, mana, position_x, position_y):
    """
    Sauvegarde 4 valeurs entières dans un fichier, une par ligne.
    Le fichier est écrasé s'il existe déjà.
    """
    try:
        # On ouvre le fichier en mode 'w' (write/écriture).
        # Cela crée le fichier ou l'écrase s'il existe.
        with open(filename, 'w') as f:
            
            # f.write() ne peut écrire que des chaînes de caractères (strings).
            # On convertit chaque entier en string et on ajoute un saut 
            # de ligne '\n' pour respecter le format "un entier par ligne".
            f.write(str(life) + "\n")
            f.write(str(mana) + "\n")
            f.write(str(position_x) + "\n")
            f.write(str(position_y) + "\n")
            
    except IOError as e:
        # Bonne pratique : gérer les erreurs si on ne peut pas écrire
        # (ex: disque plein, permissions)
        print(f"Erreur : Impossible de sauvegarder les données dans {filename}. {e}")


# retourne un tuple contenant les valeurs (life, mana, position_x et position_y) précédemment sauvegardées
def load_data(filename):
    """
    Charge 4 valeurs entières depuis un fichier, une par ligne.
    
    Lève une FileNotFoundError si le fichier n'existe pas.
    Lève une ValueError si le fichier est corrompu (contient autre 
    chose que des nombres ou est incomplet).
    
    Retourne:
        un tuple (life, mana, position_x, position_y)
    """
    
    # L'utilisation de 'with open(filename, 'r')' (mode 'r' pour read/lecture)
    # est la façon standard de gérer cela.
    # Si le fichier 'filename' n'existe pas, la fonction open()
    # lèvera *automatiquement* une FileNotFoundError.
    # La consigne est donc respectée sans devoir ajouter de code 'if'.
    
    with open(filename, 'r') as f:
        # On lit les 4 lignes, une par une
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        line4 = f.readline()
        
        # On doit convertir les lignes (qui sont des strings) en entiers.
        # .strip() enlève les caractères invisibles (comme '\n')
        # int() convertit le string "propre" en nombre entier.
        # Si le fichier est vide ou corrompu, int() lèvera une ValueError.
        life = int(line1.strip())
        mana = int(line2.strip())
        position_x = int(line3.strip())
        position_y = int(line4.strip())
        
        # On retourne les 4 valeurs dans un tuple, comme demandé.
        return (life, mana, position_x, position_y)