# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.07.2026
# Nazwa i wersja programu: class_basic.py
# W kodzie jest pokazany przykład z klasą - podstawy klas i obiektowości

# User

# name

# mail

# age

# poniższy sposób definiowania klasy działa ale nie jest prawidłowy .. nie ma konstruktora
# class User: # nazwa klasy powinna zaczynać się z dużej litery
#     def print_info(self): # metoda to funkcja przypisana do konkretnej klasy
#         print(self.name)
#         print(self.mail)
#         print(self.age)

# user = User()
# user.name = 'Jarek'
# user.mail = 'jaroslav@gmail.com'
# user.age = 35

# user1 = User()
# user1.name = 'Zenek'
# user1.mail = 'zen@gmail.com'
# user1.age = 46

# user.print_info()
# user1.print_info()

# print(user.name) # wyświetlenie wartości poszczególnych atrybutów - name
# print(user.age)  # wyświetlenie wartości poszczególnych atrybutów - age

# ---------------------- POWINNO BYĆ TAK -------------------------------------------

class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self): # metoda to funkcja przypisana do konkretnej klasy
        print(self.name)
        print(self.mail)
        print(self.age)
        

    def is_male(self):
        return self.name[-1:] != 'a'

user = User('Jaro', 'jar@gmail.com', 56)
user.print_info()
print(f"Jest mężczyzną - {user.is_male()}")
print()

user1 = User('Karolina', 'karolina@wp.pl', 34)
user1.print_info()
print(f"Jest mężczyzną - {user1.is_male()}")
print()

