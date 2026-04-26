def search_time(trace, t):
    """
    pre: une trace, un temps t
    post: l'index du premier tuple dans trace avec un temps supérieur où égal à t;
          len(trace) si un tel tuple n'existe pas
    """
    pass

def absolute(v1, v2):
    """
    pre: v1 et v2 deux nombres
    post: la fonction retourne |v1 - v2|
    """
    pass

def euclidian_distance(c1, c2):
    """
    pre: deux coordonnées c1 = (x1, y1) et c2 = (x2, y2)
    post: la fonction retourne la distance euclidienne entre c1 et c2
    """
    pass

def cross(trace1, trace2, theta1, theta2):
    """
    pre: deux traces trace1 et trace2, chacun une liste de tuples (t, (x, y)),
         deux floats theta1 et theta2
    post: retourne 1 si les traces trace1 et trace2 se croisent, ou theta1 et
          theta2 sont utilisés comme seuils, comme indiqué dans les consignes.
          Retourne 0, sinon.
    """
    for (t1, (x1, y1)) in trace1:
        for (t2, (x2, y2)) in trace2:
            if absolute(t1, t2) <= theta1 and euclidian_distance((x1, y1), (x2, y2)) < theta2:
                return 1
    return 0