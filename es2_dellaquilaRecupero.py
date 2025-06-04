class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
    
    def __str__(self):
        return f"\nDati libro:\nISBN: {self.isbn}\tTitolo: {self.titolo}\nAutore: {self.autore}\tAnno: {self.anno}"


class Biblioteca:
    def __init__(self):
        self.lista = []  # Inizializza la lista dei libri

    def aggiungi_libro(self, libro):
        self.lista.append(libro)
        print("Libro aggiunto")

    def rimuovi_libro(self, isbn):
        for libro in self.lista:
            if (libro.isbn == isbn):
                print("Rimozione del libro ",libro.titolo," dell'anno ",libro.anno)
                self.lista.remove(libro)
                break

    def elenco_libri(self):
        for libro in self.lista:
            print(libro)

    def cerca_libro(self, isbn):
        conta = 0
        for libro in self.lista:
            if (libro.isbn == isbn):
                conta = 1
                return libro
        if (conta == 0):
            return None
        
biblio = Biblioteca()
codici = []
def aggiungi():
    while True:
        isbn = str(input("Inserisci l'isbn del libro: "))
        if (isbn in codici):
            print("ISBN inserito è di un altro libro, riprova")
        else:
            codici.append(isbn)
            break
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    while True:
        anno = int(input("Inserisci l'anno': "))
        if (anno > 0 and anno < 2026):
            break
        else:
            print("Riprova, anno inserito non valido")
    return Libro(isbn, titolo, autore, anno)


while True:
    scelta = int(input("\nMenu:\n0. esci\n1. aggiungi libro\n2. rimuovi libro\n3. elenco libri\n4. cerca libro\n Scelta: "))
    if (scelta == 0):
        print("sei uscito dal programma")
        break
    elif (scelta == 1):
        nuovoLibro = aggiungi()
        print(nuovoLibro)
        biblio.aggiungi_libro(nuovoLibro)
    elif (scelta == 2):
        if (len(codici) == 0):
            print("\nLista vuota")
        else:
            isbn = str(input("Inserisci l'isbn del libro: "))
            if (isbn in codici):
                biblio.rimuovi_libro(isbn)
                codici.remove(isbn)
                print("\nLibro eliminato")
            else:
                print("ISBN non trovato.")
    elif (scelta == 3):
        if (len(codici) == 0):
            print("\nLista vuota")
        else:
            print(biblio.elenco_libri())
    elif (scelta == 4):
        if (len(codici) == 0):
            print("\nLista vuota")
        else:
            isbn = str(input("Inserisci l'isbn del libro: "))
            if (isbn in codici):
                print(biblio.cerca_libro(isbn))
            else:
                print("ISBN non trovato.")
    else:
        print("Scelta non valida, riprova")