# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.07.2026
# Nazwa i wersja programu: practical_functions.py
# W kodzie pokazane jest jak zwracać wartość z funkcji

def strip_and_uppercase(text):
    return str(text).strip().upper() # uzycie return powoduje zwrócenie wartości z funkcji



text = '   JesteM teXteM DO zmiany'
print(text)
text = strip_and_uppercase(text)
print(text)
    