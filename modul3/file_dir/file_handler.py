# Autor uczący się: Jarosław Krefft
# Data utworzenia: 15.07.2026
# Nazwa i wersja programu: file_handler.py
# W kodzie jest zaprezentowana obsługa pliku tekstowego przy odczytywaniu

#file_handler.py
with open("D:\\Szkolenia\\KB\\Python\\code\\modul3\\file_dir\\test.txt") as file:
    #file_content = file.read()  # odczytywany jest cały tekst z pliku
    #file_content = file.readline() # odczytywana jest jedna linia pliku - pierwsza
    file_content = file.readline() # otrzymujemy listę 
    print(file_content)



try:
    with open("D:\\Szkolenia\\KB\\Python\\code\\modul3\\file_dir\\test2.txt") as file2:
        for line in file2.readlines():
            print(line)
except FileNotFoundError:
    print("Plik nie został znaleziony.")


# 3 sposób odczytywania zawartości pliku tekstowego

with open("D:\\Szkolenia\\KB\\Python\\code\\modul3\\file_dir\\test.txt") as file:
    for line in file2:
        print(line)
