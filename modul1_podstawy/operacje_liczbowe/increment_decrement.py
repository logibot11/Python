# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.06.2026
# Nazwa i wersja programu: increment_decrement.py
# W kodzie są zaprezentowane działania inkrementacji i dekrementacji oraz kilka innych działań
import os

os.system("cls") # oczyszczenie ekranu

# Opis działania programu
print("Program prezentuje inkrementacje , dekrementację oraz inne skrótowe operacje.\n")

a = int(input("Podaj liczbę."))  # pobranie liczby do dalszych operacji

liczba=a
liczba+=1
print("\nWynik inkrementacji o 1 ",liczba)

liczba=a
liczba-=2
print("\nWynik dekrementacji o 2 ",liczba)

liczba=a
liczba*=3
print("\nWynik mnozenia przez 3", liczba)

print("\n **********  Koniec programu. ************\n")