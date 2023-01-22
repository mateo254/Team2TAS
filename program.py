
region = input("Podaj swój region USA/EUR: ")
plec = input("Podaj swoją płeć K/M: ")
wiek = input("Podaj wiek użytkownika: ")

if wiek.isdigit() == False:
    exit("Wiek musi być liczbą całkowitą.")

wiek = int(wiek)
region = str(region)
plec = str(plec)

if region == "USA":
    print("Twój region to USA")
    if wiek >= 21 and wiek < 30:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    elif wiek >= 30 and plec == "K":
        print("Witaj w naszej apce z alkoholem. Zapraszamy do zakupów. Mamy dla Ciebie wyjatkowy prezent. Aperol Spritz doda sie automatycznie do Twojego koszyka z zakupami")
    elif wiek >= 30 and plec == "M":
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

if region == "EUR":
    print("Twój region to EUR")
    if wiek >= 18 and wiek < 30:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    elif wiek >= 30 and plec == "K":
        print("Witaj w naszej apce z alkoholem. Zapraszamy do zakupów. Mamy dla Ciebie wyjatkowy prezent. Aperol Spritz doda sie automatycznie do Twojego koszyka z zakupami")
    elif wiek >= 30 and plec == "M":
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")



