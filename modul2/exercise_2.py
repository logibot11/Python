# Autor uczący się: Jarosław Krefft
# Data utworzenia: 07.07.2026
# Nazwa i wersja programu: exercise_2.py
# Wytyczne Kamila: Napisz program który sprawdza czy podana od użytkownika liczba jest większa od 0, mniejsza od 0 równa 0


in_val = input("Podaj dowolną liczbe całkowitą: \t")

if in_val.lstrip("-").isdigit():
    liczba = int(in_val)

    if liczba > 0:
        print(f"\nPodana liczba {liczba} jest wieksza od wartości 0")
    elif liczba < 0:
        print(f"\nPodana liczba {liczba} jest mniejsza od wartosci 0")
    elif liczba == 0:
        print(f"\nPodana liczba {liczba} jest równa wartości 0")
else:
    print("\nSorry Batory ... niestety nie podałeś liczby tylko inne znaki ... ogarnij się.")
