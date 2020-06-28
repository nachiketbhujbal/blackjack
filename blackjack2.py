import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return ("{} of {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                instatiate_card = Card(suit, rank)
                self.deck.append(instatiate_card)
    def __str__(self):
        deck_cont = ''
        for card in self.deck:
            deck_cont += '\n' + card.__str__()
        return 'The deck has: ' + deck_cont

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_one_card = self.deck.pop()
        return deal_one_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + values[self.cards[-1].rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def ace_adjust(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
    def __str__(self):
        hand_cont = ''
        for c in self.cards:
            hand_cont += '\n' + str(c) 
        return ' hand has (value: {}):'.format(self.value) + hand_cont

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet():
    my_bet = int(input("How much do you want to bet? "))

def hit(deck,hand):
    do_you_want_a_hit = str(input("Hit me? (y/n)"))
    if do_you_want_a_hit.lower() == 'y':
        hand.add_card(deck)
    if do_you_want_a_hit.lower() == 'n':
        pass
    else:
        while dealer_hand.value > 17:
            dealer_hand.add_card(playing_deck.deal())

#hit_or_stand is supposded to 'accept the deck and the player's hands as args.
#if player hits, then employ hit() function above. if stand, playing == False
def hit_or_stand(deck,hand):
    pass
    global playing #to controle an upcoming while loop
    do_you_want_a_hit = str(input("Hit me? y/n: "))
    ###add hit function....is this ncessar,...maybe bc of playing == false 
        
def show_some(player, dealer):
    player_cont = ''
    dealer_cont = ''
    dealer_hidden = []
    for c in player.cards:
        player_cont += '\n' + str(c)
        return f'Player has (Value: {player.value}): {player_cont}.'
    '''
    going to pop off the dealer's first card, then only show the rest of the cards
    '''
    print(dealer.cards)
    dealer.cards.pop(0)



def show_all(player, dealer):
    pass
def player_bust():
    pass
def player_win():
    pass
def dealer_win():
    pass
def dealer_bust():
    pass



#while True 
print("Welcome to blackjack.py...hope this works! lol :)")
playing_deck = Deck()
playing_deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()
player_hand.add_card(playing_deck.deal())
dealer_hand.add_card(playing_deck.deal())
player_hand.add_card(playing_deck.deal())    
dealer_hand.add_card(playing_deck.deal())
print(player_hand)
print(dealer_hand)
