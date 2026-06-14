# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.06.2026
# Nazwa i wersja programu: input_data_find_name.py
# Pierwsza część kodu po wpisaniu imienia wyszukuje w liście słowników podane imię - jeżeli znajdzie podaje wszystkie dane dla tego imienia
# Druga część kodu prezentuje funkcjonalność która pozwala wpisać do input kilka wartości następnie je rozdze
# Trzecia część kodu prezentuje użycie input tak że pozwala na rozpoznanie odpowiedzi -  tak / nie i dalsze działanie


# 1 - wyszukiwanie imienia w liście słowników
# ------------------------------------------------
find_opt = input("Podaj imię:")

#lista słowników
dane = [
    {"id": 1, "imie": "Ala", "zwierze": "Kot"},
    {"id": 2, "imie": "Ola", "zwierze": "Pies"},
    {"id": 3, "imie": "Jan", "zwierze": "Papuga"},
    {"id": 4, "imie": "Ala", "zwierze": "Tygrys"}
] 

# Dostęp do danych
print(dane[0]["imie"])
wyniki = [osoba for osoba in dane if osoba["imie"] == find_opt]
print(wyniki)


# 2 - Input pozwala wpisać wiele wartości po czym przy pomocy metody split rozdziela je.
# -----------------------------------------------------------------------------------------
a, b, c = input("Podaj dwie liczby: ").split()
print(a)
print(b)
print(c)

# 3 - input reakcja na wybór -  tak / nie
# ------------------------------------------------------------------------------------------
answer = input("Kontynuować? [t/n]: ").lower()
if answer == "t":
    print("Start")

