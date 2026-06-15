# Autor uczący się: Jarosław Krefft
# Data utworzenia: 15.06.2026
# Nazwa i wersja programu: check_input_temperature.py
# W kodzie sprawdzane jest temperatura dzięki operatorom logicznym

import os

os.system("cls")

temp_upper_limit = 31 # w stopniach Celsjusza
temp_low_limit = 5 # w stopniach Celsjusza

temp = int(input("Podaj wartość temperatury czujnika oznaczonego - TS001 "))

# zamiast ...if temp >= temp_low_limit and temp <= temp_upper_limit:
# poniższy zapis stosujemy gdy warunki są różne i nie da się ich zapisać jako jednego przedziału.
# wówczas musimy uzyć operatora and
if temp_low_limit <= temp <= temp_upper_limit:
    print(f"Temperatura wynosi  {temp}\u00B0 C - jest ok!. " )

elif temp > temp_upper_limit:
    print(f"\033[31m Temperatura wynosi {temp}\u00B0 C - jest zbyt wysoka. \033[0m")

elif temp < temp_low_limit:
    print(f"\033[34m Temperatura wynosi {temp}\u00B0 C - jest zbyt niska. \033[0m")

