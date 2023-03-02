# 1
def zad1():
    linia_danych = input("Wczytaj dane: ")
    separator_zrodlowy = input("Wczytaj separator źródłowy: ")
    separator_docelowy = input("Wczytaj separator docelowy: ")

    dane = linia_danych.split(separator_zrodlowy)
    dane_nowe = separator_docelowy.join(dane)

    # dane_nowe = linia_danych.replace(separator_zrodlowy,separator_docelowy)

    print(dane_nowe)


# 2
tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. ' \
        'Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. ' \
        'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. ' \
        'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty ' \
        'Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji ' \
        'druków na komputerach osobistych, jak Aldus PageMaker'

# 3
litera_1 = "Kamil"[2]
litera_2 = "Lipiński"[3]
liczba_liter1 = tekst.count(litera_1)
liczba_liter2 = tekst.count(litera_2)
print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')

# 4


