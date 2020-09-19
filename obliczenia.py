from pola import *

while True:
    print("""
        Wybierz, figurę, której pole chcesz obliczyć:

        1)Kwadratu
        2)Prostokąta
        3)Trójkąta
        4)Trapezu
        5)Rombu
        6)Koła
        7)Zakończ działanie programu

        """)
    wybor = input("Podaj nr dzialania: ")
    print()

    if wybor == '1':
        a = float(input("Podaj a: "))
        pole = kwadrat(a)
        print(pole)
    elif wybor == '2':
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        pole = prostokat(a,b)
        print(pole)
    elif wybor == '3':
        a = float(input("Podaj a: "))
        h = float(input("Podaj h: "))
        pole = trojkat(a,h)
        print(pole)
    elif wybor == '4':
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        h = float(input("Podaj h: "))
        pole = trapez(a,b,h)
        print(pole)
    elif wybor == '5':
        p = float(input("Podaj p: "))
        q = float(input("Podaj q: "))
        pole = romb(p,q)
        print(pole)
    elif wybor == '6':
        r = float(input("Podaj r: "))
        pole = kolo(r)
        print(pole)
    elif wybor == '7':
        break
    else:
        print("Podano nieprawidlowa wartosc")
        
