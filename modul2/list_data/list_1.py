# Autor uczący się: Jarosław Krefft
# Data utworzenia: 09.07.2026
# Nazwa i wersja programu: list_1.py
# W kodzie jest zaprezentowana struktura danych typu lista i podstawowe działania na niej

# Lista jest struktura danych która pozwala na duplikaty elementów o tej samej nazwie

names = ['Dominik', 'Jarek', 'Wojciech']
names.append('Dominik')

print(names) # wyświetlenie całej listy
print(names[0]) # wyświetlenie pojedyńczego elementu listy
# print(names[3]) # błędne wywołanie elementu listy poza zakresem - IndexError: list index out of range

for name in names: # wyświetlenie imion z listy przy użyciu pętli for
    print(name)

print("\nPo usunieciu elementu listy z indeksem 1")
del names[1] # usuniecie elementu spod indeksu 1
print(names)

names.remove('Dominik') # zostanie usuniete pierwsze wystąpienie elementu o danej nazwie
print(names)

print(names.count('Dominik')) # policzenie ilości wystapień elementu o danej nazwie

print(len(names)) # długośc listy .. ile elementów 

names.sort() # sortowanie elementów listy
print(names)

names.sort(reverse=True) # sortowanie w odwrotnej kolejnosci
print(names)

names.extend(['Aneta', 'Marek']) # rozszerzenie listy names o elementy z innej listy
print(names)

names[1] = 'Cezary' # podmiana danych w danej pozycji listy
print(names)