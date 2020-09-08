import random

print("NBA TOP TRUMPS")


player = []

number_of_cards1= 5
number_of_cards2 = 5

player.append(["Lebron James",27.1,7.4,7.4,38.4])
player.append(["Kevin Durant",27.0,4.1	,7.1,36.9])
player.append(["Micheal Jordan",30.1,5.3,6.2,38.3])
player.append(["James Harden",25.2,6.3,5.3,34.3])
player.append(["Kobe Bryant",25.0,4.7,5.2,36.1])
player.append(["Larry Bird",24.3,6.3,10.0,38.4])
player.append(["Shaquille O'Neal",23.7,2.5,10.9,34.7])
player.append(["Stephen Curry",23.5,6.6,4.5,34.3])
player.append(["Russell Westbrook",23.2,8.3,7.1,34.6])

while True:
    print("Your Card:")
    card1 = random.randint(0,len(player)-1)
    print("Name: " + player[card1][0])
    print("Points: " + str(player[card1][1]))
    print("Assists: " + str(player[card1][2]))
    print("Rebounds: " + str(player[card1][3]))
    print("Minutes per game: " + str(player[card1][4]))
    card2 = random.randint(0,len(player)-1)

    choice = int(input("Which criteria do you want to choose?(1-Points, 2-Assists, 3-Rebounds,4-Minutes per game)"))

    if choice == 1:
        x = player[card1][1]
        y = player[card2][1]
        z = x-y
        if z < 0:
            number_of_cards1 = number_of_cards1 - 1
            print("YOU HAVE LOST THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z == 0:
            print("YOU HAVE TIED THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z > 0:
            number_of_cards1 = number_of_cards1 + 1
            print("YOU HAVE WON THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")

    if choice == 2:
        x = player[card1][2]
        y = player[card2][2]
        z = x-y
        if z < 0:
            number_of_cards1 = number_of_cards1 - 1
            print("YOU HAVE LOST THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z == 0:
            print("YOU HAVE TIED THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z > 0:
            number_of_cards1 = number_of_cards1 + 1
            print("YOU HAVE WON THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")

    if choice == 3:
        x = player[card1][3]
        y = player[card2][3]
        z = x-y
        if z < 0:
            number_of_cards1 = number_of_cards1 - 1
            print("YOU HAVE LOST THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z == 0:
            print("YOU HAVE TIED THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z > 0:
            number_of_cards1 = number_of_cards1 + 1
            print("YOU HAVE WON THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")

    if choice == 4:
        x = player[card1][4]
        y = player[card2][4]
        z = x-y
        if z < 0:
            number_of_cards1 = number_of_cards1 - 1
            print("YOU HAVE LOST THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z == 0:
            print("YOU HAVE TIED THE ROUND YOU HAVE", number_of_cards1, "CARDS REMAINING")
        elif z > 0:
            number_of_cards1 = number_of_cards1 + 1
            print("YOU HAVE WON THE ROUND YOU HAVE", number_of_cards1, "REMAINING")
    if number_of_cards1 == 10:
        print("YOU HAVE WON")
        break
    if number_of_cards2 == 0:
        print("YOU HAVE LOST")
        break