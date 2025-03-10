import random
#punto 1
#print("Popolamento del dizionario con stampa (punto 1)")
                                                #antipasti                      primi                              secondi              \\\\desert
dizionario = {"Mario Rossi":  [("Antipasti",(8,7,9),"Junior Chef"),  ("Primi",(7,8,8),"Junior Chef"), ("Secondi",(9,9,8),"Junior Chef"), ("Dessert",(8,8,9),"Junior Chef")],
              "Luigi Bianchi":[("Antipasti",(7,7,8),"Senior Chef"),  ("Primi",(8,9,7),"Senior Chef"), ("Secondi",(7,8,7),"Senior Chef"), ("Dessert",(9,8,8),"Senior Chef")],
              "Giulia Verdi": [("Antipasti",(9,8,8),"Junior Chef"),  ("Primi",(8,7,9),"Junior Chef"), ("Secondi",(8,8,8),"Junior Chef"), ("Dessert",(7,9,8),"Junior Chef")],
              }

#punto 2 -->
#print("\nAggiunta di un nuovo chef (punto 2)")
dizionario["Francesco Dell'aquila"] = [("Antipasti",(6,8,3),"Junior Chef"),  ("Primi",(3,7,4),"Junior Chef"), ("Secondi",(6,5,4),"Junior Chef"), ("Dessert",(4,9,6),"Junior Chef")]
#print(dizionario)

#punto 3 
#print("\nAggiunta di una nuova categoria di piatto (punto 3)")
def aggiungiPiatto():
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
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    print("Stampa dei dati di uno chef (punto 4)")
    print("\nInserisci prima il nome e poi il cognome qui sotto, da così verificare i dati di quello chef")
    nom = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    nomeCerca = nom + " " + cognome
    if nomeCerca in dizionario.keys():
      print("\nLo chef richiesto è presente, ecco i suoi dati: ")
      i = 0
      for nome, portate in dizionario.items():
        if nome == nomeCerca:
            for categoriaPiatto, (creatività, gusto, presentazione), categoriaChef in portate:
              print("Categoria dello chef: ",categoriaChef)
              print("Nome e cognome dello chef:",nome)
              print(f"Punteggi {categoriaPiatto}:      \n- Creatività: ",creatività,"\n- Gusto:",gusto,"\n- Presentazione:",presentazione)
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

#punto 6 --> sistemato i due metodi e i messaggi di errore
def mediaPunteggi():
    categorieChef = ["Junior Chef","Senior Chef"]
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    chef = input(f"Inserisci la categoria di chef ({categorieChef}): ") #messo la f e richiamato l'array tramite graffe
    somma = 0
    if chef in categorieChef:
        categoria = input("\nInserisci la categoria di piatto: ")
        if categoria in categorie:
            print("Categoria inserita valida.")
            i = 0
            for nome, portate in dizionario.items():
                somma += sum(portate[i][1]) #incrementa somma
                i += 1 #conta
            media = somma / i
            return media
        else:
            print("Categoria di portate inserita non valida.")
            return 0
    else:
        print("Categoria di chef non valida")
        return 0

def punteggioTotaleMAx():
    arrayPunteggi = []
    categorieChef = ["Junior Chef","Senior Chef"]
    categorie = ["antipasti","primi","secondi","dessert","piatti unici"]
    chef = input(f"Inserisci la categoria di chef ({categorieChef}): ") #messo la f e richiamato l'array tramite graffe
    if chef in categorieChef:
        categoria = input("\nInserisci la categoria di piatto: ")
        if categoria in categorie:
            print("Categoria inserita valida.")
            i = 0
            for nome, portate in dizionario.items():
                arrayPunteggi.append(portate[i][1])
                i += 1
            punteggi = max(arrayPunteggi)
            return punteggi
        else:
            print("Categoria di portate inserita non valida.")
            return 0
    else:
        print("Categoria di chef non valida")
        return 0

def analisiPunteggi():
    punteggi = punteggioTotaleMAx()
    if punteggi == 0:
        print("Errore nel calcolo dei punteggi")
    else:
        print("Il massimo punteggi delle categoria inserite è di",punteggi)
    media = mediaPunteggi()
    if media == 0:
        print("Errore nel calcolo della media dei punteggi") 
    else:
        print("La media dei punteggi delle categoria inserite è di",media)

aggiungiPiatto() #richiamata la funzione prima del menu, così risolto il problema di errore nella stampa dello chef
while True:
    scelta = int(input("Menu\n0 - esci\n1 - stampa chef\n2 - cerca categoria di un piatto\n3 - punteggi massimi per categoria\nScelta: "))
    if scelta == 0:
        break
    elif scelta == 1:
        stampaChef()
    elif scelta == 2:
        stampaDIUnPiatto()
    elif scelta == 3:
        analisiPunteggi()
    #elif scelta == 4:
        #nominativo = inserisci_dati_nuovo_chef()
        #inserisci_nuovo_chef(dizionario,nominativo,risultati)
    else:
        print("Scelta non valida, riprova")