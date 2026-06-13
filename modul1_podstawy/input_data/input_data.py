# Autor uczący się: Jarosław Krefft
# Data utworzenia: 13.06.2026
# Nazwa i wersja programu: input_data.py
# prosty przykład pobierania danych od użytkownika oraz odczytania danych jako listy

device_name = input("Podaj nazwę sprzętu do wypżyczenia: ")
print("Nazwa ogólna: " + device_name)

words = input("Podaj 5 kolorów oddzielonych spacją:").split()
for word in words:
    print(word)

