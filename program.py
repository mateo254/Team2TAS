wiek = input("Podaj wiek użytkownika jako liczbę całkowitą: ")

plec = input("Prosze podaj swoja plec: K-kobieta albo M-mężczyzna ")
while plec.upper() != "K" and plec.upper() != "M":
    plec = input("Niepoprawna wartość. Prosze wprowadź M lub K: ")

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


