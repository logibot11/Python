# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.07.2026
# Nazwa i wersja programu: exercise_6.py
# Wytyczne Kamila: Napisz program który wyświetli sumę wszystkic liczb parzystych z przedziału 1 - 100

suma = 0

for i in range(1, 101):
    if i % 2 == 0:
        suma += i
    
print(suma)