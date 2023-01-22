wiek = input("Podaj wiek użytkownika jako liczbę całkowitą: ")
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo nie jest liczbą całkowitą ")
wiek = int(wiek)
if wiek >= 18 and wiek<=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")
elif wiek > 40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")
    print("Uważaj w Twoim wieku na alkohol.")
else:
    print("Jesteś za młody/a na alkohol.")

# Karolina
plec = input("Podaj plec: (K/M): ")
if plec == "K" or plec == "k":
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Darmowy aperol dla Ciebie kochana")
elif plec == "M" or plec == "m":
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
else:
	print("Bledna odpowiedz. Wybierz K lub M zgodnie z poleceniem.")