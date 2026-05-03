def give_money(borrowed_money, from_person, to_person, amount):
    """
    Met à jour les comptes lorsqu'une personne donne de l'argent à une autre.
    
    borrowed_money[to_person][from_person] augmentera de 'amount'.
    borrowed_money[from_person][to_person] diminuera de 'amount'.
    """
    
    # --- 1. Validation des arguments ---
    if not isinstance(borrowed_money, dict):
        raise ValueError("borrowed_money doit être un dictionnaire.")
    if not isinstance(from_person, str):
        raise ValueError("from_person doit être une chaîne de caractères (str).")
    if not isinstance(to_person, str):
        raise ValueError("to_person doit être une chaîne de caractères (str).")
    if not (isinstance(amount, int) or isinstance(amount, float)):
        raise ValueError("amount doit être un nombre (int ou float).")
    if amount < 0:
        raise ValueError("amount ne peut pas être négatif.")
    if from_person == to_person:
        raise ValueError("Une personne ne peut pas se donner de l'argent à elle-même.")

    # --- 2. Ajout des personnes si elles sont nouvelles ---
    if from_person not in borrowed_money:
        borrowed_money[from_person] = {}
    if to_person not in borrowed_money:
        borrowed_money[to_person] = {}

    # --- 3. Mise à jour des dettes (logique miroir) ---
    
    # 'to_person' doit 'amount' de PLUS à 'from_person'
    current_debt_to_from = borrowed_money[to_person].get(from_person, 0)
    borrowed_money[to_person][from_person] = current_debt_to_from + amount

    # 'from_person' doit 'amount' de MOINS à 'to_person'
    current_debt_from_to = borrowed_money[from_person].get(to_person, 0)
    borrowed_money[from_person][to_person] = current_debt_from_to - amount

def total_money_borrowed(borrowed_money):
    """
    Calcule la somme de tout l'argent actuellement emprunté (la somme
    de toutes les dettes positives).
    """
    
    if not isinstance(borrowed_money, dict):
        raise ValueError("borrowed_money doit être un dictionnaire.")

    total = 0
    
    # On parcourt le dictionnaire principal (tous les "emprunteurs")
    for borrower_name, debts in borrowed_money.items():
        if not isinstance(debts, dict):
            # Vérification de la structure interne
            raise ValueError(f"Les données pour '{borrower_name}' ne sont pas un dictionnaire.")
            
        # On parcourt le dictionnaire imbriqué (tous les "prêteurs")
        for lender_name, amount in debts.items():
            # On ajoute seulement si le montant est positif
            if amount > 0:
                total += amount
                
    return total

# --- Implémentation de l'exemple (requise par le test 'test_init') ---

# Cette variable DOIT s'appeler 'borrowed_money' 
# et être définie au niveau global pour que le test passe.
borrowed_money = {}

try:
    # Mark prête 2 000 000€ à Bill
    give_money(borrowed_money, "Mark", "Bill", 2000000)
    
    # Mark prête 2 000 000€ à Steve
    give_money(borrowed_money, "Mark", "Steve", 2000000)
    
    # Serguei prête 5 000 000€ à Bill
    give_money(borrowed_money, "Serguei", "Bill", 5000000)
    
    # Bill prête 6 000 000€ à Larry
    give_money(borrowed_money, "Bill", "Larry", 6000000)
    
    # Larry prête 5.5€ à Linus
    give_money(borrowed_money, "Larry", "Linus", 5.5)

    # Steve rembourse Mark
    give_money(borrowed_money, "Steve", "Mark", 2000000)

except ValueError as e:
    # Gère toute erreur pouvant survenir lors de l'exécution de l'exemple
    print(f"Une erreur est survenue lors de l'initialisation : {e}")