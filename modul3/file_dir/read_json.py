# Autor uczący się: Jarosław Krefft
# Data utworzenia: 17.07.2026
# Nazwa i wersja programu: read_json.py
# prosty przykład pobierania danych z pliku w formacie json

import json

text = """
[{"title": "Nauka Pythona",
"author": "Kamil Brzeziński",
"tags": ["python", "java", "C#"],
"likes": 7
},
{"title": "Nauka Javt",
"author": "John Miles",
"tags": ["C++", "js", "vba"],
"likes": 3
}]"""

# dane pobierane z pliku w formacie json
with open('D:\\Szkolenia\\KB\\Python\\code\\modul3\\file_dir\\entries.json') as json_file:
    entries = json.load(json_file)

# entries = json.loads(text) # dane pobierane ze struktury danych które sa w kodzie źródłowym
    print(entries)
    print(entries[1])
    print(entries[1]['tags'][2])
    print(entries[0]['likes'])