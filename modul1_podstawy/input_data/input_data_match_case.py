# Autor uczący się: Jarosław Krefft
# Data utworzenia: 13.06.2026
# Nazwa i wersja programu: input_data_match_case.py
# prosty przykład pobranaia opcji menu (int)

import os

os.system('cls')

print("----MENU-----")
print("1.Dodaj imie.")
print("2.Usuń imie.")
print("3.Wyświetl wszystkie.")
print("4.Wyjdź.")

opcja = int(input("\n Wybierz opcje."))

match opcja:
    case 1:
        print("Wybrano dodanie imienia. \n")
    case 2:
        print("Wybrano opcę usuń imię. \n")
    case 3:
        print("Wybrano opcję Wyświetl wszystkie. \n")
    case 4:
        print("Wybrno zakończenie programu. \n")
