# Autor uczący się: Jarosław Krefft
# Data utworzenia: 12.07.2026
# Nazwa i wersja programu: # Autor uczący się: Jarosław Krefft
# Data utworzenia: 12.07.2026
# Nazwa i wersja programu: creating_empty_set.py
# W kodzie są pokazane różne operacje na strukturze dictionary - słowniki

# słownik to struktura typu klucz - wartość
phone_book = {
    'Jarek':123908231,
    'Mariusz':234213098,
    'Daria':908123431,
    'Aniela':908213431,
    'Robert':678987123
}

# słownik jest strukturą uporzadkowaną .. od wersji Python 3.07
# elementy słownika sa przecowywane w takiej kolejności jakiej zostały wpisane

print(phone_book.get('Jarek')) # dane są odpytywane po kluczach (nazwach) nie po indeksach
print(phone_book['Aniela'])

# print(phone_book.get('Sally')) # taki sposób pobrania wyświetli - none
# print(phone_book['Sally'])# taki sposób pobrania nieistniejącego elementu zgłosi błąd

phone_book['Zdzichu'] = 342097111 # dodanie do słownika kolejnego elementu
print(phone_book) # wyświetlenie całego słownika z kluczami i wartościami do nich przyporzadkowanymi

phone_book['Zdzichu'] = 111999777
print(phone_book['Zdzichu'])

# w przypadku powtórzenia klucza ale z inną wartością .. wówczas zostanie zapisany ostatni wpis wartości dla danego klucza
phone_book = {
    'Jarek':123908231,
    'Mariusz':234213098,
    'Daria':908123431,
    'Aniela':908213431,
    'Jarek':111222444,
    'Robert':989123431
}

print(phone_book)

# usunęcie elementu ze słownika
del phone_book['Mariusz'] # w orzypadku kiedy chcemy usunąć nie istniejący z nazwy element słownika zostanie zgłoszony błąd
print(phone_book)

# usuniecie elementu ze słownika przy pomocy pop  .. instrukcja pop  zwraca także wartość usuniętego elementu
phone_book.pop('Jarek')
print(phone_book)

#  .. instrukcja pop  zwraca także wartość usuniętego elementu
deleted_phone_number = phone_book.pop('Robert234', -1)
print(deleted_phone_number)
print(phone_book)

# sposób na zwrócenie kluczy ze słownika -- nazw
for element in phone_book:
    print(element)

# sposób na wyświetlenie wartości słownika
for element in phone_book.values():
    print(element)

# sposób na wyświetlenie kluczy i ich wartości
for element in phone_book.items():
    print(element)

# sposób na wyświetlenie osobno ale w jenym napisie klucza i jego wartości
for element in phone_book.items():
    print(element[0] + ":" + str(element[1]))

print('\n')

    # 2-gi sposób na wyświetlenie osobno ale w jenym napisie klucza i jego wartości
for name, phone_number in phone_book.items():
    print(name + ":" + str(phone_number))



