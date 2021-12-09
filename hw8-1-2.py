# Author CCG 12/9/21

def blackjack(c1,c2):

    sum = int(c1) + int(c2)
    if sum >= 21:
        return("You have busted")
    if sum <= 21:
        return("You are safe")

card1 = input("What was your first cards value?")
card2 = input("What was your second cards value?")

print(blackjack(card1,card2))

print(blackjack(10,10) == "You are safe")
print(blackjack(11,10) == "You have busted")
print(blackjack(12,10) == "You have busted")
