from math import sqrt
class pagellaScolastica:
    def __init__(self, array): 
        self.array = array

    def __str__(self):
        return str(self.array)

    def __repr__(self): #punto 1
        if (len(self.array) == 0):
            print("Array vuoto")
        else:
            for elemento in self.array:
                print(elemento)

    def media(self): #punto 2
        if (len(self.array) == 0):
            print("Array vuoto")
            return None
        else:
            somma = 0
            conta = 0
            for elemento in self.array:
                somma += elemento
                conta += 1
            media = somma / conta
            return media

    def __getitem__(self, indice): #punto 3
        if (len(self.array) == 0):
            print("Array vuoto")
        else:
            if (-1 < indice < len(self.array)):
                return self.array[indice]
            else:
                return None

    def __eq__(self, array2): #punto 4
        if (len(self.array) == len(array2)):
            si = 0
            for v1, v2 in zip(self.array, array2):
                if (v1 == v2):
                    si += 1
            if (si == len(self.array)):
                return True
            else:
                return False
        else:
            print("Confronto non disponibile, i due array hanno dimensioni diverse")

    def __sub__(self, array2): #punto 5
        if (len(self.array) == len(array2)):
            nuovaPagella = []
            for v1, v2 in zip(self.array, array2):
                nuovaPagella.append(v1 - v2)
            return nuovaPagella
        else:
            return None

    def impegno(self): #punto 6
        if (len(self.array) != 0):
            potenza = 0
            for elemento in self.array:
                potenza += (elemento * elemento)
            return sqrt(potenza)
        else:
            return None
            
voti = []
print("Inserisci i voti delle materie (da 2 a 10, 0 per terminare):")
while True:
    voto = int(input("Voto: "))
    if (voto == 0):
        break
    elif (voto < 2 or voto > 10):
        print("Voto inserito non valido, riprova")
    else:
        voti.append(voto)
pagella=pagellaScolastica(voti)

print("\nPunto 1: stampa dell'array")
print(pagella)

print("\nPunto 2: ecco la media: ",pagella.media())
v = int(input("\nPunto 3: inserisci l'indice e ti dico che voto corrisponde: "))
print(pagella[v])

voti2 = []
print("\nInserisci i voti del secondo array delle materie (da 2 a 10, 0 per terminare):")
while True:
    voto = int(input("Voto: "))
    if (voto == 0):
        break
    elif (voto < 2 or voto > 10):
        print("Voto inserito non valido, riprova")
    else:
        voti2.append(voto)
print("\nPunto 4: confronto elementi dei due array. Se hanno gli stessi elementi esce TRUE altrimenti FALSE",pagella.__eq__(voti2))
print("\nPunto 5: Sottraiamo i voti nella pagella dei due array. Ecco la stampa finale: ",pagella.__sub__(voti2))
print("\nPunto 6: Ecco l'impegno dello studente nell'array iniziale: ",pagella.impegno())