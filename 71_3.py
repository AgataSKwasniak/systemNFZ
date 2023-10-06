class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentow = []

    listaPacjentow = []
    listaPrzychodni = []

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    listaChorob = []

while True:

    menu = int(input("1-Przychodnia, 2-Pacjent, 3-Koniec"))

    if menu == 1:
        przychodnia = int(input("1-dodaj przychodnie, 2-usuń przychodnię, 3-dodaj pacjenta do przychodni, 4-usuń pasjenta z przychodni, 5-lista przychodni, 6-lista pacjentów w przychodni "))

        if przychodnia == 1:
            nazwa = input("Podaj nazwe kursu: ")
            miasto = input("Podaj miasto: ")
            listaPrzychodni.append(przychodnia)
            print("Przychodnia została pomyślnie dodana")

        elif przychodnia == 2:
            nazwa = input("Podaj nazwe przychodni: ") # Nie mozna usunac kursu jezeli sa tam zapisani kursanci !!!!
            znaleziono = False
            for y in listaPrzychodni:
                if y.nazwa == nazwa:
                    znaleziono = True
                    if len(y.listaPacjentow) != 0:
                        print("Nie można usunąć tej przychodni")
                    else:
                        listaPrzychodni.remove(y)
                        print(f"Przychodnia: {nazwa} została pomyślnie usunięta")
                        break

            if znaleziono == False:
                print(f"Przychodnia o nazwie {nazwa} nie istnieje")

        elif przychodnia == 3:
            nazwa = input("Podaj nazwe przychodni: ")
            imie = input("Podaj imie pacjenta: ")
            nazwisko = input("Podaj nazwisko pacjenta: ")

            for z in listaPrzychodni:
                if z.nazwa == nazwa:
                    pacjent = Pacjent(imie, nazwisko)
                    z.listaPacjentow.append(pacjent)
                    print("Pacjent został pomyślnie dodany")

        elif przychodnia == 4:
            nazwa = input("Podaj nazwe przychodni: ")
            nazwisko = input("Podaj nazwisko pacjenta: ")
            for c in listaPrzychodni:
                if c.nazwa == nazwa:
                    for d in c.listaPacjentow:
                        if d.nazwisko == nazwisko:
                            c.listaPacjentow.remove(d)
                            print(f"Pacjent {nazwisko} został pomyślnie usunięty")

        elif przychodnia == 5:
            for x in listaPrzychodni:
                print(f"Nazwa: {x.nazwa} Miasto: {x.miasto}")

        elif przychodnia == 6:
            nazwa = input("Podaj nazwe Przychodni: ")

            for a in listaPrzychodni:
                if a.nazwa == nazwa:
                  print(a.nazwa, a.miasto)
                  for b in a.listaPacjentow:
                    print(b.imie, b.nazwisko)

        elif przychodnia == 7:
            break

    if menu == 2:
        pacjent = int(input("1-dodaj chorobę pacjentowi, 2-lista chorób pacjenta, 3-koniec"))
        if pacjent == 1:
            nazwa = input("Podaj nazwę przychodni: ")
            nazwisko = input("Podaj nazwisko pacjenta: ")

            choroba = (nazwa, miasto)
            listaChorob.append(choroba)
            print("Kurs został pomyślnie dodany")

        elif pacjent == 2:
            for x in listaChorob:
                print(f"Imię: {x.imie}, Nazwisko: {x.nazwisko}, : {x.miasto}")

        elif pacjent == 3:
            break