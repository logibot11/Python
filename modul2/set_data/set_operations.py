# Autor uczący się: Jarosław Krefft
# Data utworzenia: 12.07.2026
# Nazwa i wersja programu: set_operations.py
# W kodzie są pokazane różne operacje na strukturze set


names = {'Franek', 'Gosia', 'Ania', 'Sonia', 'Robert'}
names2 = {'Franek', 'Robert', 'Danka', 'Kinga'}


# Suma zbiorów
print(names | names2)   # użycie pipe do zsumowania dwóch zbiorów

calendar = names | names2 # użycie pipe do zsumowania dwóch zbiorów
print(calendar)

calendar2 = names.union(names2) # zsumowanie 2 zbiorów przy pomocy union
print(calendar2)


# Część wspólna - intersection części wspólne - zostają usunięte elementy wspólne z 2 zbiorów, pozostałe elementy z drugiego zbioru names2 nie są wyświetlane ponieważ nie istnieją w zbiorze names
print(names.intersection(names2))
print(names & names2)

# Różnica - difference
print(names.difference(names2))
print(names - names2)

names = {'Franek', 'Gosia', 'Ania', 'Sonia', 'Robert'}
names2 = {'Franek', 'Robert', 'Danka', 'Kinga'}

# Symetryczna różnica - symetric difference - są pobierane elementy które są w jednym secie names albo w drugim names2 ale nie będą pobierane elementy które istnieją w dwóch zbiorach jednocześnie
print(names.symmetric_difference(names2))
print(names ^ names2)





