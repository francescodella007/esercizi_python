tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 2300)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 2100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 2100)),
        ("marzo", ("mais", 946)),
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1600)),
        ("gennaio", ("mais", 855)),
        ("febbraio", ("grano", 1550)),
        ("febbraio", ("mais", 9250)),
        ("marzo", ("grano", 100)),
        ("marzo", ("mais", 96)),
    ]),
    ("Emilia_Romagna", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 840)),
        ("febbraio", ("grano", 1550)),
        ("febbraio", ("mais", 940)),
        ("marzo", ("grano", 2100)),
        ("marzo", ("mais", 946)),
    ]),
    ("Puglia", [
        ("gennaio", ("grano", 1400)),
        ("gennaio", ("mais", 860)),
        ("febbraio", ("grano", 4250)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 2160)),
        ("marzo", ("mais", 936)),
    ])
)

regioni = []
colture = []
for regione, dati in tupla_produzione_agricola:
    regioni.append(regione)
    for mese, (coltura, produzione) in dati:
        colture.append(coltura)

lista_regioni = set(regioni)
lista_colture = set(colture)


def analizza_produzione_agricola(tupla_produzione_agricola, dato1,dato2):
    somma = 0
    conta = 0
    max = 0
    max_mese = ""
    for regione, dati in tupla_produzione_agricola:
        if dato1 == regione:
            for mese, (coltura, produzione) in dati:
                if dato2 == coltura:
                    somma += produzione
                    conta += 1
                    if (produzione > max):
                        max = produzione
                        max_mese = mese
    media_produzione = somma / conta
    return (media_produzione, (max, max_mese))


while True:
    dato1 = input(f"Inserisci la regione ({lista_regioni}): ")
    dato2 = input(f"Inserisci il nome della coltura ({lista_colture}): ")
    conta1 = 0
    conta2 = 0

    for regione, dati in tupla_produzione_agricola:
        if dato1 in regione:
            conta1 += 1
            for mese, (coltura, produzione) in dati:
                if dato2 in coltura:
                    conta2 += 1
    if (conta1 > 0 and conta2 > 0):
        break
    else:
        print("Dati inseriti non validi\n")
        if (conta1 == 0):
            print("Nome della regione inserito non valido")
        if (conta2 == 0):
            print("Nome della coltura errato")


tupla_1 = analizza_produzione_agricola(tupla_produzione_agricola, dato1,dato2)
print(f"I dati di produzione media mensile e il mese con la produzione massima per quella coltura :\n{tupla_1}")