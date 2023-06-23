n = 36

"""
Erklärung des Programms (Die Erklärung wurde mithilfe von KI generiert):
Das Programm definiert mehrere Funktionen und Variablen, um das Spiel zu
simulieren und zu analysieren:
1. Die Funktion teiler(k) berechnet alle positiven Teiler der ganzen Zahl k und gibt
sie als Liste zurück.
2. Die Variable alle_teiler speichert die Liste der Teiler einer vorgegebenen Zahl n.
3. Die Variablen punkte, pfeile und farben sind leere Listen bzw. ein Wörterbuch, die
verwendet werden, um Spielzustände ("Spielsituationen"), Übergänge (Züge) und Farben für
Visualisierungszwecke zu speichern.
4. Die Funktion mögliche_züge(s) berechnet alle möglichen Züge (Spielzustände),
die vom aktuellen Spielzustand s aus erreichbar sind, und gibt sie als Liste
zurück.
5. Die Funktion speichere_züge_als_punkte(situationen) erzeugt alle möglichen
Spielzustände, die sich aus einem Zug weiter von jedem Zustand in der Liste
situationen ergeben, und speichert sie als neue Spielzustände in der Liste
punkte.
6. Die Funktion graphviz_output(dateiname) erstellt eine GraphViz-Datei (mit dem
gegebenen dateiname), die die Spielzustände und Übergänge (Züge) mithilfe
einer grafischen Darstellung repräsentiert.
7. Die Funktion letzte_situationen_rot() markiert alle letzten Züge (Zustände) als rot.
8. Die Funktion vorteilhafte_situationen_grün() markiert vorteilhafte Spielzustände
(Zustände, die zu einer Gewinnsituation führen) als grün.
9. Die Funktion unvorteilhafte_situationen_rosa() markiert nachteilige Spielzustände
(Zustände, die zu einer Verlierersituation führen) als rosa.
10. Die Funktion alle_situationen_überprüft() überprüft, ob alle Spielzustände mit einer
Farbe markiert wurden.
Das Programm initialisiert das Spiel, indem es den anfänglichen leeren Spielzustand
([]) in der Liste punkte speichert und dann alle möglichen Spielzustände, die vom
anfänglichen Zustand aus erreichbar sind, mithilfe der Funktion
speichere_züge_als_punkte() generiert.
Anschließend markiert das Programm die letzten Züge als rot mit Hilfe der Funktion
letzte_situationen_rot(). Danach markiert es iterativ vorteilhafte Spielzustände als grün und
nachteilige Spielzustände als rosa, bis alle Spielzustände markiert sind, indem es die
Funktionen vorteilhafte_situationen_grün() und unvorteilhafte_situationen_rosa() Funktionen
durchführt.
"""

def teiler(k):
    """
    Diese Funktion berechnet alle positiven Teiler der ganzen Zahl k.
    Ihr Rückgabewert ist eine Liste mit den Teilern.
    """
    t = []
    for i in range(1,int(k/2)+1):
        if k%i == 0:
            t.append(i)
    t.append(k)
    return t

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
    werden ausgerechnet. Das Ergebnis ist eine Liste aller Spielzüge,
    die aus der Spielsituation s direkt erreichbar sind.
    """
    erlaubte_züge = alle_teiler.copy()
    for t in alle_teiler:
        for z in s:
            if z%t == 0 and t in erlaubte_züge:
                erlaubte_züge.remove(t)
    möglich = []
    for t in erlaubte_züge:
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

def letzte_situationen_rot():
    """
    Färbt alle letzten Situationen rot.
    """
    letzte_situationen = punkte.copy()
    for s in punkte:
        for ü in pfeile:
            if ü[0] == s and s in letzte_situationen:
                letzte_situationen.remove(s)
    for z in letzte_situationen:
        farben[tuple(z)] = 'red'

def vorteilhafte_situationen_grün():
    """
    Färbt alle vorteilhaften Situationen grün, laut aktuellem Stand.
    """
    for s in punkte:
        grün_möglich = True
        for ü in pfeile:
            if ü[0] == s:
                nächste_situation = tuple(ü[1])
                if not (nächste_situation in farben):
                    grün_möglich = False # Es gibt keine Information über den nächsten Zug
                else:
                    if farben[nächste_situation] == 'green': # s kann nicht vorteilhaft sein
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
                nächste_situation = tuple(ü[1])
                if nächste_situation in farben and farben[nächste_situation] == 'green': # s ist nicht vorteilhaft
                    rosa = True
        if not tuple(s) in farben and rosa:
            farben[tuple(s)] = 'pink'

def alle_situationen_überprüft():
    """
    Entscheidet ob alle Situationen schon überprüft (gefärbt) wurden.
    """
    for s in punkte:
        if not(tuple(s)) in farben:
            return False
    return True

speichere_züge_als_punkte([[]])
speichere_züge_als_punkte(punkte)
letzte_situationen_rot()
while not alle_situationen_überprüft():
    vorteilhafte_situationen_grün()
    unvorteilhafte_situationen_rosa()
graphviz_output("chomp.gv")
