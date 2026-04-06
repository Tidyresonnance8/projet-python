def afficheMax(a,b):
    """
    pre: --
    post: affiche le maximum entre les nombres entiers 'a' et 'b'
    """
    if a < b:
        return b
    else:
        return a
print(afficheMax(1,12))
print(afficheMax(12,14))