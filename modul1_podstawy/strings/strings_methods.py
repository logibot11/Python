# Autor uczący się: Jarosław Krefft
# Data utworzenia: 01.07.2026
# Nazwa i wersja programu: strings_metods.py
# W kodzie są zaprezentowane metody dla klasy string

channel_name = 'jak nauczyć się programowania'
print(channel_name)

print(channel_name.upper()) # metoda upper słuzy do zamiany wszystkich małych liter w napisie na wielkie litery

print(channel_name.capitalize()) # metoda capitalize służy do zamiany pierwszej litery na dużą a wszystkie pozostałe na małe

channel_name2 = 'JaK bY Nie byŁo świat jest pięKnY'
print(channel_name2.lower()) # zamienia wszystkie litery na małe

channel_name3 = '  JaK bY Nie byŁo świat jest pięKnY        '
print(channel_name.lower().strip()) # strip usuwa spacje na początku i końca

print(channel_name.startswith("j")) # sprawdza  poczatek tekstu ... czy istnieje litera lub ciąg znaków w tekście
print(channel_name.endswith("a")) # sprawdza  koniec tekstu ... czy istnieje litera lub ciąg znaków w tekście

# ====================== strip() - usuwa spacje z poczatku i końca 
tekst_strip =  "   StripPython   "
print(tekst_strip.strip())

# ===================== lstrip() - usuwa spacje z lewej strony
tekst_lstrip = "   LeftStripPython   "
print(tekst_lstrip.lstrip())

# ===================== rstrip() - usuwa spacje z prawej strony
tekst_rstrip = "   StripPythonRight   "
print(tekst_rstrip.rstrip())

# ====================== count liczy wystapienia np. litery =============================
tekst1 = "dojrzała banana" 
print(tekst1.count("a"))

# ====================== join - łaczy elementy listy  ===================================
jezyki = ["Pyton", "SQL", "Spark"]
print(" | ".join(jezyki))

tekst1 = "dojrzała banana"
print(tekst1.find("r")) # find zwraca indeks pierwszego wystapienia litery znaku

# ====================== index() - podobnie jak find() ale zgłasza wyjatek gdy nie znajdzie tekstu
tekst3 = "Python"
print(tekst3.index("t"))


# ====================== isaplha() - sprawdza czy napis zawiera wyłacznie litery =========================================
tekst4 = "Python"
print(tekst4.isalpha())

# ====================== isdigit() - sprawdza czy napis zawiera wyłacznie cyfry ===========================================
tekst5 = "12345"
print(tekst5.isdigit())

# ==================== isalnum() - sprawdza czy napis zawiera tylko litery i cyfry
tekst6 = "Python12345"
print(tekst6.isalnum())

# ==================== center() - wypośrodkowuje tekst =====================================================================
tekst3 = "Python"
print(tekst3.center(20, "-"))

# ==================== replace() - 
print(channel_name.replace("programowania", "jazdy na nartach"))

# ================== split() - 
print(channel_name.split(" "))