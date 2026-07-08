# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.07.2026
# Nazwa i wersja programu: exercise_9.py
# Wytyczne Kamila: Pobierz od uzytkownika 3 liczby całkowite i uporządkuj je w kolejnosci od najmniejszej do największej)

# Pobranie trzech liczb całkowitych od użytkownika
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

liczby = [liczba1, liczba2, liczba3] # umieszczenie liczb w strukturze listy

liczby = sorted(liczby) # sortowanie od najmniejszej do największej

print(liczby) # prezentacja uporządkowanej listy liczb
