tupla_vendite = (
    (("RepartoA", "Informatica"), ("Prodotto A", ("contanti", 1000))),
    (("RepartoA", "Informatica"), ("Prodotto B", ("carta di credito", 1500))),
    (("RepartoA", "Informatica"), ("Prodotto C", ("carta di credito", 1200))),
    (("RepartoA", "Informatica"), ("Prodotto D", ("contanti", 800))),
    (("RepartoA", "Informatica"), ("Prodotto E", ("contanti", 800))),
    (("RepartoA", "Informatica"), ("Prodotto F", ("N/D", 200))),
    (("RepartoB", "Elettronica"), ("Prodotto A", ("contanti", 1500))),
    (("RepartoB", "Elettronica"), ("Prodotto B", ("carta di credito", 900)))
)

reparti = []
categorie = []
prodotti = []
tipoPagamento = []
totaleSoldi = []

for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
    reparti.append(reparto)
    categorie.append(categoria)
    prodotti.append(prodotto)
    tipoPagamento.append(tipoDiPagamento)
    totaleSoldi.append(importo)

set_reparti = set(reparti)
set_categorie = set(categorie)
set_prodotti = set(prodotti)
set_tipoPagamento = set(tipoPagamento)
somma_totaleSoldi = sum(totaleSoldi)

def media_globale(tupla_vendite):
    somma = 0
    conta = 0
    for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
        somma += importo
        conta += 1
    importo_medio = somma / conta
    return importo_medio

def media(tupla_vendite, scelta1, scelta2):
    somma = 0
    conta = 0
    for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
        if (scelta1 == categoria) and (scelta2 == tipoDiPagamento):
            somma += importo
            conta += 1
    if conta == 0:
        return 0
    mediaF = somma / conta
    return mediaF

def vendita_max(tupla_vendite):
    vendita_max = 0
    prodotto_max = None
    for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
        if importo > vendita_max:
            vendita_max = importo
            prodotto_max = prodotto
    return (vendita_max, prodotto_max)

def vendita_min(tupla_vendite):
    vendita_min = float('inf')
    prodotto_min = None
    for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
        if importo < vendita_min:
            vendita_min = importo
            prodotto_min = prodotto
    return (vendita_min, prodotto_min)

while True:
    scelta = int(input("\nMenu:\n0. esci\n" +
                       "1. stampa della tupla\n" +
                       "2. media globale\n" +
                       "3. media\n" +
                       "4. vendita massima\n" +
                       "5. vendita minima\nScelta: "))

    if scelta == 0:
        print("Sei uscito dal programma")
        break
    elif scelta == 1:
        for ((reparto, categoria), (prodotto, (tipoDiPagamento, importo))) in tupla_vendite:
            print((reparto, categoria), (prodotto, (tipoDiPagamento, importo)))
    elif scelta == 2:
        media_importi = media_globale(tupla_vendite)
        print(f"La media degli importi è di € {media_importi}")
    elif scelta == 3:
        scelta1 = input(f"Inserisci la categoria ({set_categorie}): ")
        scelta2 = input(f"Inserisci la tipologia di pagamento ({set_tipoPagamento}): ")
        calcolo_media = media(tupla_vendite, scelta1, scelta2)
        if calcolo_media == 0:
            print("Categoria o metodo di pagamento inserito non valido")
        else:
            print(f"La media degli importi per la categoria '{scelta1}' e tipologia di pagamento '{scelta2}' è di € {calcolo_media}")
    elif scelta == 4:
        max_vendita, max_prodotto = vendita_max(tupla_vendite)
        print(f"La vendita massima è di € {max_vendita} per il prodotto '{max_prodotto}'")
    elif scelta == 5:
        min_vendita, min_prodotto = vendita_min(tupla_vendite)
        print(f"La vendita minima è di € {min_vendita} per il prodotto '{min_prodotto}'")
    else:
        print("SCelta non valida")