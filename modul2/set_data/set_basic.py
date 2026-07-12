# Autor uczący się: Jarosław Krefft
# Data utworzenia: 12.07.2026
# Nazwa i wersja programu: set_basic.py
# W kodzie są pokazane działania na strukturze typu set

names = {'Jarek', 'Heniek', 'Jurek'} # utworzenie setu w którym elementy nie są uporządkowane 
print(names)

zenskie_imiona = {'Barbara', 'Inka', 'Joanna', 'Barbara'} # set nie wyświetla powtórzonych elementów -  ale też nie zgłasza żadnych komunikatów - po prostu wycina powtórzone
print(zenskie_imiona)

names.add('Rafał') # dodanie nowego elementu setu
print(names) 

names.remove('Heniek') # usinięcie elementu z setu
print(names)

for name in names: # wylistowanie elementów setu w petli for
    print(name)

names.update(['Darek', 'Janek']) # dodanie elementów będących listą do setu 
print(names)