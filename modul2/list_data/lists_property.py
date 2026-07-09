# Autor uczący się: Jarosław Krefft
# Data utworzenia: 09.07.2026
# Nazwa i wersja programu: lists_property.py
# W kodzie jest zaprezentowana struktura danych typu lista i podstawowe działania na niej

list_property = ["Uporządkowana"]
list_property.append("Modyfikowalna")
list_property.append("Może zawieraś różne typy")
list_property.append("Pozwala na duplikaty")
list_property.append("Dynamiczny rozmiar")
list_property.append("Może zawierać inne listy.")
list_property.append("Obsługuje indeksowanie i wycinanie (slicing).")
list_property.append("Można po niej iterować za pomocą pętli")

print("\nWłaściwości listy:\n")

for element in range (1, len(list_property)):
    print(f"{element}. {list_property[element]}")