# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.06.2026
# Nazwa i wersja programu: jezyk_dynamicznie_silnie_typowany.py
# W kodzie są zaprezentowane 

def add(a, b):
    print(a + b)

# a = 2 # w pierwszej wersji do zmiennej a była przyporzadkowana zmienna typu int
# b = 5 # w pierwszej wersji do zmiennej b była przyporzadkowana zmienna typu int

a = 'johny' # w dynamicznym typowaniu mozna zmienić typ zmiennej np. z int na string
b = 'wick'  # w dynamicznym typowaniu mozna zmienić typ zmiennej np. z int na string

# silne typowanie polega na tym że jeżeli do zminnej zostanie przyporzadkowana wartość typu string to do końca programu tak zostanie 
# .. chyba że znowu nastapi nowe przypisanie innego typu zmiennej

add(a, b)


a = 10
b = 'Kraków'
print(str(a) + b)  # w tym miejscu nie został zmieniony typ zmiennej a .. tylko jej zachowanie ... jest nadal typu int


print(type(a)) # odczytanie typu zmiennych przed operacją dodania i konwersji
print(type(b)) # odczytanie typu zmiennych przed operacją dodania i konwersji
a = 15
b = '7'
print(a + int(b)) # w tym miejscu nie został zmieniony typ zmiennej b .. tylko jego zachowanie ... jest nadal typu string

print(type(a)) # odczytanie typu zmiennych po operacji dodania i konwersji
print(type(b)) # odczytanie typu zmiennych po operacji dodania i konwersji

#gdybyśmy chcieli zmienić typ zmiennej b ... należałoby zrobić jak poniżej
b = int(b)
print(type(b))

# poniżej przykład redeklaracji zmiennej podając wartość innego typu
c = 2
print(type(c))

c = 'Jarek'
print(type(c))

c = True
print(type(c))