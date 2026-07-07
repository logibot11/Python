# Napisz program który zapyta użytkownika o wynik na egzaminie od 0 do 100 i wyświetli odpowiednią ocenę
#    90 - 100 -> 5
#    80 - 89  -> 4
#    70 - 79  -> 3
#    60 - 69  -> 2
#    poniżej 60 -> 1

# wyjaśnienie działania match-case
#case x if 0 <= x <= 10: oznacza:
# zapisz wartość do zmiennej x,
# sprawdź warunek po if,
# jeśli jest prawdziwy, wykonaj ten case.


punkty = int(input("Podaj ilość otrzymanych punktów na egzaminie: "))
        

match punkty:
    case x if x > 100:
        print("\nIlość punktów nie może być większa niż 100\n")

    case x if 90 <= x <= 100:
        print("\nOtrzymałeś ocenę - 5\n")

    case x if 80 <= x <= 89:
        print("\nOtrzymałes ocenę - 4\n")

    case x if 70 <= x <= 79:
        print("\nOtrzymałeś ocenę  - 3\n")
    
    case x if 60 <= x <= 69:
        print("\nOtrzymałeś ocenę  - 2\n")

    case x if  x <= 60:
        print("\nOtrzymałeś ocenę  - 1\n")

    