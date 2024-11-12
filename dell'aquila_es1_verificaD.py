#                     nomeChef, nomepiatto, punteggio, numero di giudici valutato 
tupla_competizioni = (("ChefA", "Piatto1", 8.5, 5),
                      ("ChefB", "Piatto2", 7.2, 4),
                      ("ChefC", "Piatto3", 9.0, 6),
                      ("ChefA", "Piatto4", 7.8, 5),
                      ("ChefB", "Piatto5", 8.1, 4))

nomeChef = []
nomePiatto = []
punteggio = []
num_giudici = []

for (nome, piatto, voto, numGiudici) in tupla_competizioni:
    nomeChef.append(nome)
    nomePiatto.append(piatto)
    num_giudici.append(numGiudici)

nomi_Chef = set(nomeChef)
nomi_piatti = set(nomePiatto)


def media_punteggio_competizioni(tupla_competizioni):
    for (nome, piatto, voto, numGiudici) in tupla_competizioni:
        punteggio.append(voto)
    totale_punteggio = sum(punteggio)
    persone = len(nomi_Chef)
    media = totale_punteggio / persone
    return media 

def media_punteggio_chef(tupla_competizioni, chef):
    somma = 0
    conta = 0
    for (nome, piatto, voto, numGiudici) in tupla_competizioni:
        if nome == chef:
            somma += voto
            conta += 1
    media = somma / conta
    return media

def competizione_con_piu_giudici(tupla_competizioni):
    max = 0
    max_nome = []
    max_piatto = ""
    max_punteggio = 0
    for (nome, piatto, voto, numGiudici) in tupla_competizioni:
        if numGiudici > max:
            max = numGiudici
            max_nome.append(numGiudici)
            max_piatto = piatto
            max_punteggio = voto
    set_max_nome = sum(max_nome)
    return (set_max_nome, max_piatto, max_punteggio, max)

def competizione_con_meno_giudici(tupla_competizioni):
    min = 20
    min_nome = []
    min_piatto = ""
    min_punteggio = 0
    for (nome, piatto, voto, numGiudici) in tupla_competizioni:
        if numGiudici < min:
            min = numGiudici
            min_nome.append(numGiudici)
            min_piatto = piatto
            min_punteggio = voto
    set_min_nome = sum(min_nome)
    return (set_min_nome, min_piatto, min_punteggio, min)

while True:
    scelta = int(input("\nMenu:\n"+
                "0. esci\n"+
                "1. visualizza la media del punteggio\n"+
                "2. visualizza la media del punteggio dello chef\n"+
                "3. visualizza la tupla con più giudici\n"+
                "4. visualizza la tupla con meno giudici\nScelta: "))

    if (scelta == 0):
        print("\nSei uscito dal programma\n")
        break

    elif (scelta == 1):
        media_punteggio_totale = media_punteggio_competizioni(tupla_competizioni)
        print(f"\nLa media di tutti gli chef è di {media_punteggio_totale}")

    elif (scelta == 2):
        chef = input(f"\nInserisci il nome dello chef {nomi_Chef}: ")
        conta = 0
        for (nome, piatto, voto, numGiudici) in tupla_competizioni:
            if chef in nome:
                conta += 1
        if (conta != 0):
            media_punteggio = media_punteggio_chef(tupla_competizioni, chef)
            print(f"La media del punteggio delle competizioni è di {media_punteggio}")
        else:
            print("Chef inserito non trovato.")
       
    elif (scelta == 3):
        tupla_max = competizione_con_piu_giudici(tupla_competizioni)
        print(f"\nCompetizione con più giudici:\n{tupla_max}")

    elif (scelta == 4):
        tupla_min = competizione_con_meno_giudici(tupla_competizioni)
        print(f"\nCompetizione con meno giudici:\n{tupla_min}")
    else:
        print("Scelta non valida")