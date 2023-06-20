n = 6

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

# Farben für die Punkte (als Wörterbuch):
farben = dict()

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

def graphviz_output(dateiname):
    """
    Erstellt eine GraphViz-Datei mit dateiname, die die Punkte und die Pfeile enthält.
    """
    d = open(dateiname, "w")
    d.write("digraph G {\n")
    for p in pfeile:
        d.write(f"\"{p[0]}\" -> \"{p[1]}\";\n")
    for s in punkte:
        if tuple(s) in farben:
            farbe = farben[tuple(s)]
            d.write(f"\"{s}\" [color = {farbe}; style = filled];\n")
    d.write("}\n")
    d.close()

def letzte_züge_rot():
    """
    Färbt alle letzten Züge rot.
    """
    letzte_züge = punkte.copy()
    for s in punkte:
        for ü in pfeile:
            if ü[0] == s and s in letzte_züge:
                letzte_züge.remove(s)
    for z in letzte_züge:
        farben[tuple(z)] = 'red'

def vorteilhafte_situationen_grün():
    """
    Färbt alle vorteilhaften Situationen grün, laut aktuellem Stand.
    """
    for s in punkte:
        grün_möglich = True
        for ü in pfeile:
            if ü[0] == s:
                nächster_zug = tuple(ü[1])
                if not (nächster_zug in farben):
                    grün_möglich = False # Es gibt keine Information über den nächsten Zug
                else:
                    if farben[nächster_zug] == 'green': # s kann nicht vorteilhaft sein
                        grün_möglich = False
        if not tuple(s) in farben and grün_möglich:
            farben[tuple(s)] = 'green'

def unvorteilhafte_situationen_rosa():
    """
    Färbt alle unvorteilhaften Situationen rosa, laut aktuellem Stand.
    Die letzten Züge bleiben rot.
    """
    for s in punkte:
        rosa = False
        for ü in pfeile:
            if ü[0] == s:
                nächster_zug = tuple(ü[1])
                if nächster_zug in farben and farben[nächster_zug] == 'green': # s ist nicht vorteilhaft
                    rosa = True
        if not tuple(s) in farben and rosa:
            farben[tuple(s)] = 'pink'

def alle_situationen_überprüft():
    """
    Entscheidet ob alle Situationen schon überprüft (gefärbt) wurden.
    """
    fertig = True
    for s in punkte:
        if not(tuple(s)) in farben:
            return False
    return True

speichere_züge_als_punkte([[]])
speichere_züge_als_punkte(punkte)
letzte_züge_rot()
while not alle_situationen_überprüft():
   vorteilhafte_situationen_grün()
   unvorteilhafte_situationen_rosa()
graphviz_output("chomp.gv")
