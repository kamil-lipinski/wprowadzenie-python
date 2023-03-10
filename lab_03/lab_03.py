import string

# 1
# Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej
# liście a pozostałe 5 znalazło się w nowej liście.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowa_lista1 = lista1[5:]
lista1 = lista1[:5]
print(f'lista: {lista1}')
print(f'nowa lista: {nowa_lista1}')

# 2
# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i
# wyświetl listę posortowaną malejąco.

lista2 = lista1 + nowa_lista1
lista2.insert(0, 0)
lista2_kopia = lista2.copy()
lista2.sort(reverse=True)
print(f'\nlista2: {lista2}')
print(f'lista2_kopia: {lista2_kopia}')

# 3
# Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funckję input().
# Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.

tekst = input("\nWczytaj tekst: ")
znaki = []
for i in tekst:
    if i not in znaki:
        znaki.append(i.lower())

znaki.sort()
print("".join(znaki))

# 4
# Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) a wartościami nazwy polskich miesięcy.

slownik4 = {1: "Styczen", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec", 7: "Lipiec", 8: "Sierpień",
            9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}

# 5
# Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy.
# Połącz teraz słowniki tak, żeby przykładowo dla kwietnia,
# dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

slownik5 = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
            9: "September", 10: "October", 11: "November", 12: "December"}

months = {'pl': slownik4, 'en': slownik5}
print(f'\n{months["pl"][4]}')
print(months['en'][4])

# 6
# Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, który będzie
# zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1.
# Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}

ciag = 'Marianna'
litery = []
for i in ciag:
    if i not in litery:
        litery.append(i)

slownik6 = dict.fromkeys(litery, 1)
print(f'\n{slownik6}')

# 7
# Wykorzystaj moduł string i następnie:
# - wczytaj ze standardowego wejścia dowolny łańcuch znaków,
# - używając formatowania znaków wyświetl ile oraz jaki % znaków (zamienionych na małe litery) z
# wprowadzonego tekstu pokrywa się z: string.ascii_lowercase, string.digits.

lancuch = input("\nWczytaj lancuch znaków: ").lower()

znaki1 = []
znaki2 = []

ile1 = 0
ile2 = 0

for i in lancuch:
    if i in string.ascii_lowercase:
        ile1 += 1
        if i not in znaki1:
            znaki1.append(i)
    elif i in string.digits:
        ile2 += 1
        if i not in znaki2:
            znaki2.append(i)


print(f'Pokrycie z string.ascii_lowercase: {ile1/len(lancuch):.0%}, ile znaków: {len(znaki1)}')
print(f'Pokrycie z string.digits: {ile2/len(lancuch):.0%}, ile znaków: {len(znaki2)}')
