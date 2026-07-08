# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.07.2026
# Nazwa i wersja programu: exercise_5.py
# Wytyczne Kamila: Napisz program który wyświetli wszystkie liczy pierwsze od 1 do 100


# pętla przechodzi przez wszystkie liczby od 2 do 100 - wpisana jest wartość 101 ponieważ górna granica nie jest uwzględniana
for liczba in range(2, 101):

    # przyjmujemy że liczba sprawdzana jest liczba pierwszą
    # gdy znajdziemy dzielnik tej liczby inny niż 1 lub ona sama zmienimy wartość na False 
    liczba_pierwsza = True 

    # teraz sparawdzamy wszystkie możliwe dzielniki liczby
    # w tej pętli nie sprawdzamy dzielenia liczby przez samą siebie ponieważ jest to oczywiste
    for dzielnik in range(2, liczba):

        # operator % modulo oblicza resztę z dzielenia
        # jeżeli reszta wynosi 0, oznacza to że liczba jest podzielna przez aktualny dzielnik
        if liczba % dzielnik == 0:

            # kiedy zostanie znaleziony dzielnik jest tożsamym że liczba nie jest pierwsza
            liczba_pierwsza = False
            break

    # po zakończeniu sprawdzania wszystkich dzielników 
    # sprawdzamy wartość zmiennej "liczba_pierwsza" 
    if liczba_pierwsza:
        print(liczba, end=" ") # z racji lepszego odczytu liczb - obok siebie korzystam z parametru end=" "
