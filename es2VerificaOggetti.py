class Pagella:
    def __init__(self, array):
        self.array = array

    def inserisciVoti(self, voti):
        self.array = voti
        #print(self.array)

    def __repr__(self):
        return f"Voti:\n{self.array}"
    
    def media(self):
        somma = 0
        if (len(self.array) == 0):
            print("Nessun voto presente")
        else:
            conta = len(self.array)
            somma = sum(self.array)
            media = somma / conta
            print("La media dei voti è di ",media)

    def __gititem__(self, indice): #punto 3
        conta = 0
        if (len(self.array) == 0):
            print("Non è presente nessun voto")
        else:
            for elemento in self.array:
                if (elemento <= len(self.array)):
                    print("Voto preso nella posizione richiesta: ",self.array[indice])
                    conta = 1
            if (conta == 0):
                print("Indice assegnato non corrispondente a nessun voto")
    
    def __eq__(self,voti2): #punto 4
        if (len(self.array) == 0):
            print("Non è presente nessun voto")
        else:
            no = 0
            si = 0
            for elemento in zip(self.array, voti2):
                if (self.array != voti2):
                    no += 1
                else:
                    si += 1
            if (si == (len(self.array)+1)):
                return True
            else:
                return False

    def __sub__(self, voti2):
        nuovaPagella = []
        if (len(self.array) == len(voti2)):
            for elementi in zip(self.array, voti2):
                sottrazione = self.array - voti2
                nuovaPagella.append(sottrazione)
        else:
            print("Array di diverse dimensioni, non posso fare nulla")
    
    def impegno():
        pass

                
print("Inserisci i voti di ogni materia (da 2 a 10), digita 0 per terminare: ")
voti = []
while True:
    voto = int(input("Inserisci un voto: "))
    if (voto == 0):
        break
    elif (voto < 2 or voto > 10):
        print("Voto inserito non valido, riprova")
    else:
        voti.append(voto)

pagella = Pagella(voti)

pagella.inserisciVoti(voti)
print("\nStampa della pagella (punto 1): ")
print(pagella)
print("\nMedia dei voti (punto 2): ")
pagella.media()
indice = int(input("\nInserisci l'indice e ti dico il voto (punto 3): "))
pagella.__gititem__(indice)

voti2 = []
print("\nVoti 2")
while True:
    voto = int(input("Inserisci un voto: "))
    if (voto == 0):
        break
    elif (voto < 2 or voto > 10):
        print("Voto inserito non valido, riprova")
    else:
        voti.append(voto)

print("\nConfronto tra la prima e seconda lista di voti (punto 4)")
uguale = pagella.__eq__(voti2)
print("Voti1 e voti2 sono uguale (true) o diversi (false): ",uguale)

print("\nNuova classe pagella (punto 5)")
pagella.__sub__(voti2)