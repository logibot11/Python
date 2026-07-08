# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.07.2026
# Nazwa i wersja programu: exercise_8.py
# Wytyczne Kamila: Napisz program który sprawdzi czy podane imię jest imieniem męskim czy żeńskim (załóż, że imiona żeńskie kończą się na literę a)

name  = input("Podaj imię męskie lub żeńskie.")

if name.endswith("a"):
    print(f"\nImię {name} jest żeńskim imieniem.")
else:
    print(f"\nImię {name} jest męskim imieniem.")