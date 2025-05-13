class Macchina:
    def __init__(self, targa, marca, modello, anno):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def __str__(self):
        return f"Dati veicolo\nMarca: {self.marca}\tModello: {self.modello}\nTarga: {self.targa}\tAnno: {self.anno}"

class Garage:
    def __init__(self):
        self.autoParcheggiate = []

    def aggiungi_macchina(self, macchina): # Aggiunge una macchina alla lista
        self.autoParcheggiate.append(macchina)

    def rimuovi_macchina(self, targa):
        conta = 0
        if (len(self.autoParcheggiate) == 0):
            print("\nNessuna auto parcheggiata")
        for macchina in self.autoParcheggiate:
            if(macchina.targa == targa):
                conta = 1
                self.autoParcheggiate.remove(macchina)
                print("\nAuto eliminata")
            if (conta == 0):
                print("Targa non trovata")

    def elenco_macchine(self):
        if (len(self.autoParcheggiate) == 0):
            print("\nNessuna auto parcheggiata")
        for macchina in self.autoParcheggiate:
            print(macchina)

    def cerca_macchina(self, targa):
        conta = 0
        if (len(self.autoParcheggiate) == 0):
            print("\nNessuna auto parcheggiata")
        for macchina in self.autoParcheggiate:
            if(macchina.targa == targa):
                conta = 1
                print(macchina)
            if (conta == 0):
                print("Targa non trovata")

garage = Garage()
targhe = []
def aggiungiDati():
    print("\nAggiugi auto nel parcheggio")
    marca = input("Inserisci la marca: ")
    modello = input("Inserisci il modello: ")
    while True:
        targa = input("Inserisci la targa: ")
        if (targa in targhe):
            print("Targa non valida, è già presente. Riprova")
        else:
            if (len(targa) == 7): 
                targhe.append(targa)
                break
            else:
                print("Targa inserita in lunghezza non valida")
    while True:
        anno = int(input("Inserisci l'anno di produzione: "))
        if (anno > 1920):
            break
        else:
            print("Anno di produzione non valido, riprova")

    return Macchina(targa, marca, modello, anno)

while True:
    scelta = int(input("\nMenu:\n0. esci"
                        "\n1. aggiungi auto al parcheggio"
                        "\n2. rimuovi auto  "
                        "\n3. mostra tutte le auto del garage  "
                        "\n4. cerca auto"
                        "\nScelta: "))
    
    if (scelta == 0):
        break
    elif (scelta == 1):
        auto = aggiungiDati()
        garage.aggiungi_macchina(auto)
    elif (scelta == 2):
        targa = input("Inserisci la targa: ")
        garage.rimuovi_macchina(targa)
    elif (scelta == 3):
        garage.elenco_macchine()
    elif (scelta == 4):
        targa = input("Inserisci la targa: ")
        garage.cerca_macchina(targa)
    else:
        print("Scelta inserita non valida, riprova")
