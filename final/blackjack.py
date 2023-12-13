""""(1) The Simple Game Program1"""

import random

print("Welcome to the world's simplest game!\n")

again = None

class Player(object):
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
    def ask_yes_no(question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response
    def ask_number(question, low, high):
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

while again != "n":
    players = []
    Player = num
    Player.num = ask_number(question = "How many players? (2 - 5): ", low = 2, high = 5)
    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        Player.player = __init__(name, score)
        players.append(player)
        print("\nHere are the game results:")
    for player in players:
        print(player)
    Player.again = ask_yes_no(question ="\nPlay again? (y/n): ")
    
input("\n\nPress the enter key to exit.")

""""(2) The Simple Game Program2"""

class BJ_Card(Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else: 
            v = None
        return v
        
class BJ_Deck(Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.append(BJ_Card(rank, suit))

class BJ_Hand(Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

def __str__(self):
    rep=self.name+":\t"+super(BJ_Hand,self).__str__()
    if self.total:
        rep += "(" + str(self.total) + ")"
    return rep
    @property

    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value

    contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True


    if contains_ace and t <= 11:
        t += 10 # add only 10 since we add 1 to Ace
    return t
    
    def is_busted(self):
        return self.total > 21

    class BJ_Player(BJ_Hand):
        def is_hitting(self):
            response = ask_yes_no("\n" + self.name +", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")
        
    def push(self):
        print(self.name, "pushes.")

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
            self.dealer = BJ_Dealer("Dealer")
            self.deck = BJ_Deck()
            self.deck.populate()
            self.deck.shuffle()
        @property

def still_playing(self):
    sp = []
    for player in self.players:
        if not player.is_busted():
            sp.append(player)
        return sp

def __additional_cards(self, player):
    while not player.is_busted() and player.is_hitting():
    self.deck.deal([player])
    print(player)
    if player.is_busted():
        player.bust()

def play(self):
    self.deck.deal(self.players + [self.dealer],per_hand=2)
    self.dealer.flip_first_card() # hide dealer 1st card
    for player in self.players:
        print(player)
    print(self.dealer)
    for player in self.players:
        self.__additional_cards(player)
    self.dealer.flip_first_card()
    if not self.still_playing:
        print(self.dealer)
    else:
        print(self.dealer)
        self.__additional_cards(self.dealer)
    if self.dealer.is_busted():
        for player in self.still_playing:
            player.win()
    else:
        for player in self.still_playing:
            if player.total > self.dealer.total:
                player.win()
            elif player.total < self.dealer.total:
                player.lose()
            else:
                player.push()
    for player in self.players:
        player.clear()
    self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = ask_number("How many players? (1 - 7): ", low = 1, high = 8)

for i in range(number):
    name = input("Enter player name: ")
    names.append(name)
print()

game = BJ_Game(names)
again = None
while again != "n":
    game.play()
    again=ask_yes_no("\nWant to play again?:")

main()
input("\n\nPress the enter key to exit.")

""""(3) blackjackgame"""

class Card:
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply

class Hand:
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            reply = ""
            for card in self.cards:
                reply += str(card) + "\t"
        else:
            reply = "<empty>"
        return reply
        
    def clear(self):
        self.cards = []
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck:
    """ A deck of playing cards. """
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

    def clear(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            reply = ""
            for card in self.cards:
                reply += str(card) + "\t"
        else:
            reply = "<empty>"
        return reply



deck1 = Deck()
print("Created a new deck.")
print("Deck:")
print(deck1)
deck1.populate()
print("\nPopulated the deck.")
print("Deck:")
print(deck1)
deck1.shuffle()
print("\nShuffled the deck.")
print("Deck:")
print(deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand = 5)
print("\nDealt 5 cards to my hand and your hand.")
print("My hand:")
print(my_hand)
print("Your hand:")
print(your_hand)
print("Deck:")
print(deck1)
deck1.clear()
print("\nCleared the deck.")
print("Deck:", deck1)
print("\n\nPress the enter key to exit.")

""""(4) 너무 어려운 """
