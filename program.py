wiek = input("Podaj wiek użytkownika jako liczbę całkowitą: ")
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo nie jest liczbą całkowitą ")

#Zamiana wieku na typ int
wiek = int(wiek)


#Obsługa bugu z zerowym wiekiem
if wiek == 0:
    wiek = wiek + 1


#Walidacja wieku
if wiek >= 18 and wiek<=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")

elif wiek > 40:
    print("Witaj w naszej apce z alkoholem, zapraszamy na zakupy.")

    print("Uważaj w Twoim wieku na alkohol.")
else:
    print("Jesteś za młody/a na alkohol.")