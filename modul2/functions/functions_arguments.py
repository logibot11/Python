# Autor uczący się: Jarosław Krefft
# Data utworzenia: 09.07.2026
# Nazwa i wersja programu: functions_arguments.py
# W kodzie jest zaprezentowana struktura danych typu lista i podstawowe działania na niej


# argumenty pozycyjne 

def hello(name, age, last_name=None):  # parametr opcjonalny - last_name=None
    print('Cześć ' + name + ' ! Masz ' + str(age) + " lat. ")
    if last_name is not None:
        print('Masz na nazwisko ' + last_name)

# argumenty pozycyjne ... name ..jako pierwszy i ..age.. jako drugi
hello('Heniek', 45, 'Nowak')

# argumenty kluczowe .. najpierw podajemy klucz a potem wartość
hello(age=35, name='Edek') # argumenty kluczowe