# Autor uczący się: Jarosław Krefft
# Data utworzenia: 15.06.2026
# Nazwa i wersja programu: convert_to_binary.py
# W kodzie jest zaprezentowana konwersja liczby dziesietnej do binarnej uprzednio  pobranej od uzytkownika

n = int(input("Wpisz liczbę do konwersji."))
bity = ""

while n > 0:
    bity = str(n % 2) + bity    
    # poniżej jest dzielenie całkowite (floor division) - część ułamkowa jest odrzucana
    n //= 2 

print(bity)
