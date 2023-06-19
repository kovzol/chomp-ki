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

# Alle Übergänge (als Liste von Listen):
pfeile = []

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
            pfeile.append([s, neue_situation])
    return möglich

def speichere_züge_als_punkte(situationen):
    """
    Alle situationen werden um einen Zug weitergespielt und als weitere Punkte gespeichert.
    """
    for s in situationen:
        mz = mögliche_züge(s)
        for z in mz:
            if not (z in punkte):
                punkte.append(z)

def graphviz_output():
    print("digraph G {")
    for p in pfeile:
        print(f"\"{p[0]}\" -> \"{p[1]}\";")
    print("}")

speichere_züge_als_punkte([[]])
#print(punkte)
speichere_züge_als_punkte(punkte.copy())
#print(punkte)
#print(pfeile)
graphviz_output()
