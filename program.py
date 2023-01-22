
region = input("Podaj swój region USA/EUR: ")
plec = input("Prosze podaj swoja plec: K-kobieta albo M-mężczyzna ")
while plec.upper() != "K" and plec.upper() != "M":
    plec = input("Niepoprawna wartość. Prosze wprowadź M lub K: ")
wiek = input("Podaj wiek użytkownika: ")


if wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo nie jest liczbą całkowitą ")
#Zamiana wieku na typ int
wiek = int(wiek)

if wiek >= 18 and wiek<=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")
elif wiek > 40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")
    print("Uważaj w Twoim wieku na alkohol.")
else:
    print("Jesteś za młody/a na alkohol.")

region = str(region)
plec = str(plec)

#Obsługa bugu z zerowym wiekiem
if wiek == 0:
    wiek = wiek + 1

if region == "USA":
    print("Twój region to USA")
    if wiek >= 21 and wiek < 30:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    elif wiek >= 30 and (plec == "K" or plec == "k"):
        print("Witaj w naszej apce z alkoholem. Zapraszamy do zakupów. 
        Mamy dla Ciebie wyjatkowy prezent. Aperol Spritz doda sie automatycznie do Twojego koszyka z zakupami")
        print("Darmowy aperol dla Ciebie kochana")
    elif wiek >= 30 and (plec == "M" or plec == "m"):
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

