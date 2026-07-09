# Autor uczący się: Jarosław Krefft
# Data utworzenia: 09.07.2026
# Nazwa i wersja programu: combining_lists.py
# W kodzie jest pokazany sposób na połączenie dwóch list na dwa sposoby

# 1. Przy pomocy metody extend

# Lista imion męskich
list_male = ["Jan", "Piotr", "Adam", "Mietek", "Franek"]
list_female = ["Hania", "Basia", "Linda", "Ula", "Aniela"]

list_male.extend(list_female)

# Wyświetlenie połączonej listy
print("\nPołączona lista przy pomocy metody extend:")
print(list_male)

# 2. Za pomocą operatora + 
list_male = ["Jan", "Piotr", "Adam", "Mietek", "Franek"]
list_female = ["Hania", "Basia", "Linda", "Ula", "Aniela"]

# Połączenie list
all_names = list_male + list_female

# Wyświetlenie połączonej listy
print("\nPołączona lista imion przy pomocy operatora +:")
print(all_names)