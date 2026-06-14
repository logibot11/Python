# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.06.2026
# Nazwa i wersja programu: operacje_liczbowe.py
# W kodzie są zaprezentowane pobieranie liczb typu int od uzytkownika oraz proste operacje matematyczne na pobranyc liczbach

import os

# oczyszczenie ekranu
os.system('cls')

# Opis działania programu
print("Program po wpisaniu 2 liczb wykonuje kilka prostych operacji matematycznych.\n")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie ")
print("4. Dzielenie")
print("5. Obliczanie modulo")
print("\n")

# Pobranie danych od użytkownika do realizacji kilku operacji liczbowych 
a, b = map(int, input("Podaj dwie liczby oddzielone spacją: ").split())
print("Wartości podanych liczb a = ", a, " b = ", b)

c = a + b
print("\n 1. Wynik dodawania a + b = " , c)

c = a - b
print("\n 2. Wynik odejmowania a - b = " , c)

c = a * b
print("\n 3. Wynik mnozenia a * b = " , c)

c = a / b
print("\n 4. Wynik dzielenia a / b = " , c)

c = a % b
print("\n 5. Wynik modulo a '%' b = " , c)

print("\n Koniec programu.\n")

