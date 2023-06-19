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
alle_teiler = teiler(n)

# Alle Spielsituationen (als Liste von Listen):
punkte = []

def mögliche_züge(s):
    """
    Alle Spielsituationen, die aus der Spielsituation s direkt erreichbar sind,
    werden ausgerechnet und als eine Liste rückgegeben.
    """
    erlaubte_züge = alle_teiler.copy()
    for t in alle_teiler:
        for z in s:
            if z%t == 0 and t in erlaubte_züge:
                erlaubte_züge.remove(t)
    möglich = []
    for t in alle_teiler:
        if t in erlaubte_züge:
            neue_situation = s.copy()
            neue_situation.append(t)
            möglich.append(neue_situation)
    return möglich

punkte.append([6]) # [6] ist ein Start des Spieles
print(mögliche_züge(punkte[0]))
