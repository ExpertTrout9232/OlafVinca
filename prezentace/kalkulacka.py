print("Vitejte v Kalkulace!\n")
pokracovat = True
while pokracovat:
    prvnicislo = 0
    druhecislo = 0
    vysledek = 0
    prvnicislo = float(input("Zadejte prvni cislo: "))
    druhecislo = float(input("Zadedjte druhe cislo: "))
    print("1 - scitani")
    print("2 - odcitani")
    print("3 - nasobeni")
    print("4 - deleni")
    print("5 - mocneni")
    print("6 - odmocnovani")
    print("7 - exit")
    cislooperace = int(input("Zadejte cislo operace: "))
    if cislooperace == 1:
        vysledek = prvnicislo + druhecislo
        print("Jejich soucet je: ", vysledek)
    elif cislooperace == 2:
        vysledek = prvnicislo - druhecislo
        print("Jejich rozdil je: ", vysledek)
    elif cislooperace == 3:
        vysledek = prvnicislo * druhecislo
        print("Jejich soucin je: ", vysledek)
    elif cislooperace == 4:
        vysledek = prvnicislo / druhecislo
        print("Jejich podil je: ", vysledek)
    elif cislooperace == 5:
        vysledek = prvnicislo ** druhecislo
        print("Jejich mocnina je: ", vysledek)
    elif cislooperace == 6:
        vysledek = prvnicislo ** (1/druhecislo)
        print("Jejich odmocnina je: ", vysledek)
    elif cislooperace == 7:
        pokracovat = False
    else:
        print("Neplatna volba!")
input("\nUkonceni libovolnou klavesou...")
