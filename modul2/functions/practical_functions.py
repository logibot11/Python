# Autor uczący się: Jarosław Krefft
# Data utworzenia: 14.07.2026
# Nazwa i wersja programu: practical_functions.py
# W kodzie jest uzasadnienie po co uzywamy funkcji

countries_information = {}
countries_information['Polska'] = ('Warszawa', 38)
countries_information['Niemcy'] = ('Berlin', 83)
countries_information['Francja'] = ('Paryż', 57)


def print_country_information(country):
    print('Kraj - ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkańców: ' + str(countries_information[country][1]) + ' milionów')
    print()

print_country_information('Polska')
print_country_information('Francja')
print_country_information('Niemcy')