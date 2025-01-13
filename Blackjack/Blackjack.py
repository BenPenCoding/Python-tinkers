from random import *

cards = ["Ace","Ace","Ace","Ace",
         "Two","Two","Two","Two",
         "Three","Three","Three","Three",
         "Four","Four","Four","Four",
         "Five","Five","Five","Five",
         "Six","Six","Six","Six",
         "Seven","Seven","Seven","Seven",
         "Eight","Eight","Eight","Eight",
         "Nine","Nine","Nine","Nine",
         "Ten","Ten","Ten","Ten",
         "Jack","Jack","Jack","Jack",
         "Queen","Queen","Queen","Queen",
         "King","King","King","King",
         "Ace","Ace","Ace","Ace",
         "Two","Two","Two","Two",
         "Three","Three","Three","Three",
         "Four","Four","Four","Four",
         "Five","Five","Five","Five",
         "Six","Six","Six","Six",
         "Seven","Seven","Seven","Seven",
         "Eight","Eight","Eight","Eight",
         "Nine","Nine","Nine","Nine",
         "Ten","Ten","Ten","Ten",
         "Jack","Jack","Jack","Jack",
         "Queen","Queen","Queen","Queen",
         "King","King","King","King"]

#(Two decks)

value = {"One":1,"Two":2, "Three":3, "Four":4, "Five":5,
         "Six":6, "Seven":7, "Eight":8, "Nine":9,"Ten":10,
         "Eleven":11, "Jack":10, "Queen":10, "King":10}

def getValue(card):
    return value[card]

def getPlayerTotal(cards):
    total = 0
    for card in cards:
        if card == "Ace":
            total += int(input("You have an ace, enter either 1 or 11: "))
        else:
            total += getValue(card)
    return total

def getBotTotal(cards):
    total = 0
    for card in cards:
        if card == "Ace":
            if cards.index(card) == 0:
                otherCard = cards[1]
            else:
                otherCard = cards[0]
            if isPlayerBust(["Eleven",otherCard]):
                total += 1
            else:
                total += 11
        else:
            total += getValue(card)
    return total

def isBlackjack(cards):
    if (("Ten" in cards) or ("Jack" in cards) or ("Queen" in cards) or ("King" in cards)) and "Ace" in cards:
        return True
    else:
        return False

def isPlayerBust(cards):
    if getPlayerTotal(cards) > 21:
        return True

def isBotBust(cards):
    if getBotTotal(cards) > 21:
        return True
    else:
        return False

def shuffleCards(cards):
    newDeck = []
    for i in range(52):
        newDeck.append(cards.pop(randint(0,52-i-1)))
    return newDeck

def firstDeal(cards):
    newCards = []
    for i in range(2):
        newCards.append(cards.pop(randint(0,len(cards)-len(newCards))))
    return newCards

def hitDeal(cards):
    newCard = ""
    newCard = cards.pop(randint(0,len(cards)))
    return newCard

def Play():
    playerValue = 0
    botValue = 0

    playerCards = [] + firstDeal(cards)
    botCards = [] + firstDeal(cards)

    print(f"Bot's cards are: {botCards[0]}, and HIDDEN.")
    print(f"Your cards are: {playerCards[0]}, and {playerCards[1]}.")
    
    playerValue = getPlayerTotal(playerCards)
    botValue = getBotTotal(botCards)

    print(f"Your total is: {playerValue}.")

    if isBlackjack(botCards):
        if isBlackjack(playerCards):
            return "Push"
        else:
            return "Bot wins, blackjack"
    elif isBlackjack(playerCards):
        return "Player wins, blackjack"
    
    while True:
        hit = False
        if str(input("Type y to hit, anything else to stick: ")) == "y":
            hit = True
        
        if hit == True:
            playerCards.append(hitDeal(cards))
            playerValue = getPlayerTotal(playerCards)
            print(f"Your total is: {playerValue}.")
            if isPlayerBust(playerCards):
                return "Bot wins"
        else:
            break
    
    print(f"Bot's cards are: {botCards[0]}, and {botCards[1]}.")
    
    while botValue < 17:
        botCards.append(hitDeal(cards))
        botValue = getBotTotal(botCards)
        print(f"Bot's cards are: {botCards}.")
        if isBotBust(botCards):
            return "Player wins"
    if botValue > playerValue:
        return "Bot wins"
    elif playerValue > botValue:
        return "Player wins"
    else:
        return "Push"
    
print(Play())
