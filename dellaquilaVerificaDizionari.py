import random
#punto 1 
print("Popolamento del dizionario con stampa (punto 1)")
                                                #antipasti                      primi                              secondi              \\\\desert
dizionario = {"Mario Rossi":  [("Antipasti",(8,7,9),"Junior Chef"),  ("Primi",(7,8,8),"Junior Chef"), ("Secondi",(9,9,8),"Junior Chef"), ("Dessert",(8,8,9),"Junior Chef")],
              "Luigi Bianchi":[("Antipasti",(7,7,8),"Senior Chef"),  ("Primi",(8,9,7),"Senior Chef"), ("Secondi",(7,8,7),"Senior Chef"), ("Dessert",(9,8,8),"Senior Chef")],
              "Giulia Verdi": [("Antipasti",(9,8,8),"Junior Chef"),  ("Primi",(8,7,9),"Junior Chef"), ("Secondi",(8,8,8),"Junior Chef"), ("Dessert",(7,9,8),"Junior Chef")],
              }

#punto 2 --> 
print("\nAggiunta di un nuovo chef (punto 2)")
dizionario["Francesco Dell'aquila"] = [("Antipasti",(6,8,3),"Junior Chef"),  ("Primi",(3,7,4),"Junior Chef"), ("Secondi",(6,5,4),"Junior Chef"), ("Dessert",(4,9,6),"Junior Chef")]
#print(dizionario)

#punto 3
def aggiuntaPiatto():
    print("\nAggiunta di una nuova categoria di piatto (punto 3)")
    for nome, portate in dizionario.items():
        cat = portate[0][2]
        n1=random.randint(1,10)
        n2=random.randint(1,10)
        n3=random.randint(1,10)
        nuovaPortata = ("Piatti Unici",(n1,n2,n3),cat)
        dizionario[nome].append(nuovaPortata)
    #print("DAti aggiunti correttamente, ecco la stampa:\n",dizionario)

#punto 4
def stampaChef():
    print("Stampa dei dati di uno chef (punto 4)")
    print("Inserisci prima il nome e poi il cognome qui sotto, da così verificare i dati di quello chef")
    nom = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    nomeCerca = nom + " " + cognome
    if nomeCerca in dizionario.keys():
        print("Lo chef richiesto è presente, ecco i suoi dati: ")
        for nome, portate in dizionario.items():
            if nome == nomeCerca:
                print("Categoria dello chef: ",portate[0][2])
                print("Nome e cognome dello chef:",nome)
                print("Punteggi antipasti:      \n- Creatività: ",portate[0][1][0],"\n- Gusto:",portate[0][1][1],"\n- Presentazione:",portate[0][1][2])
                print("Punteggi primi:          \n- Creatività: ",portate[1][1][0],"\n- Gusto:",portate[1][1][1],"\n- Presentazione:",portate[1][1][2])
                print("Punteggi secondi:        \n- Creatività: ",portate[2][1][0],"\n- Gusto:",portate[2][1][1],"\n- Presentazione:",portate[2][1][2])
                print("Punteggi dessert:        \n- Creatività: ",portate[3][1][0],"\n- Gusto:",portate[3][1][1],"\n- Presentazione:",portate[3][1][2])
                print("Punteggi piatti unici:   \n- Creatività: ",portate[4][1][0],"\n- Gusto:",portate[4][1][1],"\n- Presentazione:",portate[4][1][2])
    else:
        print("Il nome inserito non è corretto")

#punto 5
def stampaDIUnPiatto():
    i = 0
    print("\nInserisci una categoria di chef e ti mostra i dati dei chef")
    piatto = input("Inserisci la categoria di portata: ")
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    if piatto in categorie:
        print("Categoria inserita valida, ecco i chef che ne fanno parte")
        for nome, portate in dizionario.items():
            print("\nNome dello chef:",nome)
            if piatto == "antipasti":
                print("Punteggi: ",portate[i][1])
            elif piatto == "primi":
                print("Punteggi: ",portate[i][1])
            elif piatto == "secondi":
                print("Punteggi: ",portate[i][1])
            elif piatto == "dessert":
                print("Punteggi: ",portate[i][1])
            else:
                print("Punteggi: ",portate[i][1])
    else:
        print("Categoria inserita non valida")

#punto 6
def mediaPunteggi():
    arrayPunteggi = []
    categorieChef = ["Junior Chef","Senior Chef"]
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    chef = input("Inserisci la categoria di chef (",categorieChef,"): ")
    if chef in categorieChef:
        categoria = input("\nInserisci la categoria di piatto: ")
        if categoria in categorie:
            print("Categoria inserita valida.")
            i = 0
            for nome, portate in dizionario.items():
                arrayPunteggi.append(portate[i][1])
                i += 1
            sommaPunteggi = sum(arrayPunteggi)
            media = sommaPunteggi / 5
            return media
        else:
            print("Categoria di portate inserita non valida.")
    else:
        print("Categoria di chef non valida")
    
def punteggioTotaleMAx():
    arrayPunteggi = []
    categorieChef = ["Junior Chef","Senior Chef"]
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    chef = input("Inserisci la categoria di chef (",categorieChef,"): ")
    if chef in categorieChef:
        categoria = input("\nInserisci la categoria di piatto: ")
        if categoria in categorie:
            print("Categoria inserita valida.")
            i = 0
            for nome, portate in dizionario.items():
                arrayPunteggi.append(portate[i][1])
                i += 1
            maxPunteggi = max(arrayPunteggi)
            punteggi = arrayPunteggi[0]+arrayPunteggi[1]+arrayPunteggi[2]
            return punteggi
        else:
            print("Categoria di portate inserita non valida.")
    else:
        print("Categoria di chef non valida")

def analisiPunteggi():
    punteggi, nomi = punteggioTotaleMAx()
    print("Il massimo punteggi delle categoria inserite è di",punteggi,"con i chef che sono: ",nomi)
    media = mediaPunteggi()
    print("La media dei punteggi delle categoria inserite è di",media)

while True:
    scelta = int(input("Menu\n0 - esci\n1 - aggiungi piatto\n2 - stampa chef\n3 - cerca categoria di un piatto\nScelta: "))
    if scelta == 0:
        break
    elif scelta == 1:
        aggiuntaPiatto()
    elif scelta == 2:
        stampaChef()
    elif scelta == 3:
        stampaDIUnPiatto()
    elif scelta == 4:
        analisiPunteggi()
    else:
        print("Scelta sbagliata")