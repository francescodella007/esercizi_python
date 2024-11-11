tupla = (("Milano", [("gennaio", 10),("febbraio", 2)]),
         ("Brescia", [("gennaio", 5),("febbraio", 4)]),
         ("Como", [("gennaio", 2),("febbraio", 3)]),
         ("Pavia", [("gennaio", 0),("febbraio", 2)]))


def precipitazioni(tupla, scelta):
    somm = []
    quanMin = 15
    quanMax = 0
    quantità_max = []
    quantità_min = []
    mese_max = []
    mese_min = []
    for città, dati in tupla:
        if città == scelta:
            for mese, quantita in dati:
                somm.append(quantita)
                if quantita != "N/D":
                    if quantita > quanMax:
                        quanMax = quantita
                        quantità_max.append(quantita)
                        mese_max.append(mese)
                    if quantita < quanMin:
                        quanMin = quantita
                        quantità_min.append(quantita)
                        mese_min.append(mese)
    somma = sum(somm)
    media = somma / len(somm)
    max_mese = set(mese_max)
    min_mese = set(mese_min)
    max_quantità = set(quantità_max)
    min_quantità = set(quantità_min)
    return media,(max_quantità, max_mese),(min_quantità, min_mese)

conta = 0
scelta = str(input("Inserisci il nome della città: "))
for città, *dati in tupla:
    if scelta == città:
        conta += 1 
if conta != 0:
    ritorno = precipitazioni(tupla, scelta)
    print(f"Media precipitazioni: {ritorno}")
else:
    print("La città non è presente nella tupla.")