# Autor uczący się: Jarosław Krefft
# Data utworzenia: 03.07.2026
# Nazwa i wersja programu: petla_while.py
# W kodzie jest zaprezentowana pętla while - 3 przypadki użycia

# ======================= 1. Przypadek - drukowanie wartości w pętli (podnoszenie o 1) ===========================================
i = 1

while i < 5:
    print(i)
    i += 1

# ======================= 2. Przypadek - Oczekiwanie w pętli while na wpisanie odpowiedniego imienia =================================

name = None

while name != 'Jarek':
    name = input("Jak masz na imię?")

print("O cześć Jarek")

# ====================== 3. Przypadek - Menu Programu ==================================================================================

while True:
    print("\nMENU")
    print("1. Dodaj użytkownika")
    print("2. Wyświetl uzytkowników")
    print("3. Wyjście")

    wybor = input("Wybierz opcję:  ")
    
    if wybor == "1":
        print("Dodawanie ...")
    elif wybor == "2":
        print("Lista użytkowników ...")
    elif wybor == "3":
        print("Koniec programu")
        break
    else:
        print("Niepoprawny wybór.")
