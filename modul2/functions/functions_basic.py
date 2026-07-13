# Autor uczący się: Jarosław Krefft
# Data utworzenia: 13.07.2026
# Nazwa i wersja programu: functions_basic.py
# W kodzie są pokazane podstawy funkcji

def hello(name): # w momencie deklaracji funkcji mówimy o parametrze
        print('Cześć ' + name + '!')

def show(name, age): # parametry funkcji
        print(f"Jestem {name} mam {age} lat. Pozdrawiam Serdecznie")
        


hello('Jarek') # w momencie wykorzystania konkretnej wartości w funkcji mówimy o argumencie
hello('Franek') # w momencie wykorzystania konkretnej wartości w funkcji mówimy o argumencie

show('Heniek', 45)

