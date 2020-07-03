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


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
    def take_bet(self):
        while True:
            try:
                my_bet = int(input("How much do you want to bet? (Chips: {}) ".format(self.total)))
                self.bet = 0 + my_bet
            except ValueError:
                print("Must be integer!")
                continue
            else:
                if my_bet > self.total:
                    print("You only have {}".format(self.total))
                else:
                    break



def hit(deck,player, dealer):
    global playing
    while True:
        if player.value < 21:
            x = input("Hit me? (y/n) ")
            if x.lower() == 'y':
                player.add_card(deck.deal())
                player.ace_adjust()
                show_some(player, dealer)   
            if x.lower() == 'n':
                print("dealer turn")
                playing = False

        
        
def show_some(player, dealer):
    player_cont = ''
    dealer_cont = ''
    dealer_hidden = ''
    for c in player.cards:
        player_cont += '\n' + str(c)
    print('PLAYER 1 (VALUE: {})\nCARDS: {}'.format(player.value, player_cont))
    for num, c in enumerate(dealer.cards):
        if num == 0:
            dealer_hidden += str(c)
        if num > 0:
            dealer_cont += '\n' + str(c)
    print('DEALER CARDS: {}'.format(dealer_cont))

def show_all(player, dealer):
    dealer_all = dealer_cont + dealer_hidden
    print('DEALER (VALUE:{})\nCARDS: {}'.format(dealer.value, dealer_all))
    print('PLAYER 1 (VALUE: {})\nCARDS: {}'.format(player.value, player_cont))

def player_bust(player, dealer, player_chip):
    print("PLAYER LOSES!!!!!!!!")
    player_chip.lose_bet()
    print("Player has {}".format(player_chip.total))    
def player_win(player, dealer, player_chip):
    print("PLAYER WINS!!!!")
    player_chip.win_bet()
    print("Player has {}".format(player_chip.total))
    
def dealer_win(player, dealer, player_chip):
    print('DEALER WINS!!!')
    player_chip.lose_bet()
    print("Player has {}".format(player_chip.total))
    
def dealer_bust(player, dealer, player_chip):
    print('DEALER LOSES!)')
    player_chip.win_bet()
    print("Player has {}".format(player_chip.total))
    
def push(player,dealer):
    print("Players tie.")



try:
    while True:
        print("Welcome to blackjack.py...hope this works! lol :)")
        player_chip = Chips()
        playing_deck = Deck()
        playing_deck.shuffle()
        
        player_chip.take_bet()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(playing_deck.deal())
        dealer_hand.add_card(playing_deck.deal())
        player_hand.add_card(playing_deck.deal())    
        dealer_hand.add_card(playing_deck.deal())
        show_some(player_hand, dealer_hand)

        while playing:
            if player_hand.value < 21:
                hit(playing_deck, player_hand,dealer_hand)
            if player_hand.value > 21:
                player_bust(player_hand,dealer_hand,player_chip)
                break
        if player_hand.value <= 21:
            while dealer_hand.value > 17:
                dealer_hand.add_card(playing_deck.deal())
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chip)
        if dealer_hand.value < player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chip)
        if player_hand.value < dealer_hand.value:
            player_win(player_hand,dealer_hand,player_chip)
        else:
            push(player_hand,dealer_hand)
    
        new_game = input("Play again? y/n: ")

        if new_game.lower() == 'y':
            playing = True
            continue
        if new_game.lower() == 'n':
            print("See you soon!")
            break


except KeyboardInterrupt:
    print("\nok stopping bye :-(")