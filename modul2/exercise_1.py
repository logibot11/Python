# Autor uczący się: Jarosław Krefft
# Data utworzenia: 07.07.2026
# Nazwa i wersja programu: exercise1.py
# Napisz program który sprawdza czy podana przez użytkownika liczba jest parzysta czy nie parzysta.


in_value = int(input("Podaj dowolną liczbę całkowitą."))

if in_value % 2 == 0:
    print(f"Liczba {in_value} jest parzysta.")
else:
    print(f"Liczba {in_value} jest nie parzysta.")