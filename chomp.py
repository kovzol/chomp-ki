n = 36

def teiler(k):
    """
    Diese Funktion berechnet alle positiven Teiler der ganzen Zahl k.
    Sein Rückgabewert ist eine Liste mit den Teilern.
    """
    t = []
    for i in range(1,int(k/2)+1):
        if k%i == 0:
            t.append(i)
    t.append(k)
    return t

# Beispiel:
print(teiler(n))
