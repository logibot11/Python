# Autor uczący się: Jarosław Krefft
# Data utworzenia: 02.07.2026
# Nazwa i wersja programu: match_case.py
# W kodzie pokazane jest podstawowe użycie natch_case w rozpoznawaniu błedów 

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Nie znaleziono strony")
    case 500:
        print("Błąd serwera")