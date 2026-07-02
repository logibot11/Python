# Autor uczący się: Jarosław Krefft
# Data utworzenia: 02.07.2026
# Nazwa i wersja programu: conditional_instructions.py
# W kodzie są zaprezentowane instrukcje warunkowe if, elif, else

light = input("Jakie jest światło? (zielone, żółte, czerwone)")

if light == 'zielone':
    print("Możesz jechać")
elif light == 'żółte':
    print("Przygotuj się!")
elif light == 'czerwone':
    print("Stój!")

else:
    print("Niewłaściwy kolor")