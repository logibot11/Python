
# Autor uczący się: Jarosław Krefft
# Data utworzenia: 22.06.2026
# Nazwa i wersja programu: boolean_type.py
# W kodzie jest zaprezentowany sposób użycia zmiennej boolean na przykładzie logiki czujki ruchu zintegrowanej z naświetlaczem

detect_activity = False
is_night = True


if detect_activity and is_night:
    print("Włącz oświetlenie ogrodowe.")
else:
    print("Brak reakcji systemu oświetlenia")