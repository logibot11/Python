# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.07.2026
# Nazwa i wersja programu: exercise_10.py

# Wytyczne Kamila: Stwórz grę, w której wylosujesz liczbę z przedziału 1 - 100, zapiszesz tę liczbę w zmiennej, a nastepnie poprosisz użytkownika o odgadnięcie tej liczby
# Po każdej próbie wyświetlaj informację, czy liczba podana przez użytkownika jest mniejsza czy większa od wylosowanej.
# Gdy uzytkownik odgadnie liczbę zakończ grę.
# Znajdź informację w jaki sposób losować liczby całkowite w Pythonie.

import random
import os


liczba_uzytkownika = 0
liczba_prob = 0
liczba = random.randint(1, 100)
print(f"Program wygenerował liczbę z przedziału od 1 do 100. ")

while liczba != liczba_uzytkownika: 
    liczba_uzytkownika = int(input("Zgadnij liczbę która została wylosowana. "))
    number += 1
    os.system("cls")  
    if liczba_uzytkownika < liczba:
        print("Liczba podana przez Ciebie jest mniejsza od liczby wygenerowanej przez program.")

    elif liczba_uzytkownika > liczba:
        print("Liczba podana przez Ciebie jest większa od liczby wygenerowanej przez program.")   

    elif liczba_uzytkownika == liczba:
        print(f"Hurra udało się liczba którą podałeś {liczba_uzytkownika} jest taka sama jaką wygenerował program.\n")
        print(f"Próbowałeś {liczba_prob} razy.\n")
        break

