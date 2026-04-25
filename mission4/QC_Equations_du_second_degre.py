def solution(a, b, c):
    """
    pre:  a, b et c sont 3 nombres réels
    post: la valeur de retour de cette fonction dépend du nombre
            de solutions de l'équation ax^2 + bx + c = 0.
    - 0 solution: retourne la liste vide
    - 1 solution: retourne une liste contenant la solution de l'équation
    - 2 solutions: retourne une liste contenant les deux solutions,
                    la plus petite solution en première place
    """
    pass

def solveur(equations):
    solutions = []
    if len(equations) == 0:
        return []
    for equation in equations:
        if len(equations) != 3:
            return []
        else:
            a,b,c = equation
            sol = solution(a,b,c)
            solutions.append(sol)
        return solutions
    
    

            