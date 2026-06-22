
# Autor uczący się: Jarosław Krefft
# Data utworzenia: 22.06.2026
# Nazwa i wersja programu: boolean_type.py
# W kodzie jest zaprezentowany sposób użycia zmiennej boolean na przykładzie logiki czujki ruchu zintegrowanej z naświetlaczem



detect_activity_garden = True # wykrycie ruchu w ogrodzie
detect_activity_garage = False # wykrycie ruchu na podjeździe do garażu
is_night = True

garden_sensor = False #stan czujnika ruchu w ogrodzie 
garage_sensor = False # stan czujnika ruchu na podjeździe do garażu


if detect_activity_garden and is_night:
    print("Włącz oświetlenie ogrodowe.")
    garden_sensor = True

if detect_activity_garage and is_night:
    print("Włącz oświetlenie na podjeździe garażowym.")
    garage_sensor = True

if garden_sensor or garage_sensor:
    print("Uwaga pojawił się obiekt ruchomy na posesji!")