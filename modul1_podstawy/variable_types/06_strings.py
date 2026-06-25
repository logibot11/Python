# Autor uczący się: Jarosław Krefft
# Data utworzenia: 25.06.2026
# Nazwa i wersja programu: 06_strings.py
# W kodzie są zaprezentowane sposoby tworzenia zmiennej string i użycie interpolacji stringa przy pomocy f

name = "Jarek"
last_name = 'Krefft'
print(f"Mam na imię {name} i nazywam się {last_name}")

channel_text = 'Jak nauczyć sie programowania'
print(channel_text)

text = "Bardzo mi sie podoba ten kurs i mam zamiar go ukończyć"
print(text)


my_string =  'Jerry\'s channel' # uzycie escape character
print(my_string)

my_string2 = "Jerry's channel" # użycie cudzysłowu i w tym znak apostrofu
print(my_string2)

long_text = """"To jest niesamowicie 
długi text
        ale nie jest jednak taki długi jak
            
        by się wydawało"""
print(long_text)

long_text_apostrof = '''No i mamy
inny text a własciwie liste:
1. Sliwka
2. Gruszka
3. Wiśnia'''
print(long_text_apostrof)

str1 = 'Luke'
str2 = 'Han'
str3 = 'Leia'

# użycie interpolacji stringa przy pomocy literki f
long_fstring = f"""Lista gwiezdnych przyjaciół:
                   {str1},                 
                   {str2},          
                   {str3}."""
print(long_fstring)


a = 3
b = 4

wynik = f"Wykonamy teraz opecaję matematyczną dodawania a + b.  Gdzie a = {a} i b = {b} a wynik wynosi {a + b}"
print(wynik)


