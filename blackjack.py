import random

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
    }


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return ("{} of {}".format(self.rank, self.suit))


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six',
             'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
             'Queen', 'King', 'Ace']

    def __init__(self):
        print("Shuffling Cards... Please wait.")

        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                card = Card(suit, rank)
                self.deck.append(card)

        self.shuffle()


    def __str__(self):
        deck_cont = ''
        for card in self.deck:
            deck_cont += '\n' + card.__str__()

        return 'The deck has: ' + deck_cont

    def shuffle(self):
        random.seed()
        random.shuffle(self.deck)

    def deal(self):
        deal_one_card = self.deck.pop()
        return deal_one_card


class Chips:

    def __init__(self):
        self.total = None
        while not isinstance(self.total, int):
            try:
                bankroll = input('What is the size of your bankroll? > ')
                self.total = int(bankroll)
            except Exception as e:
                print('Whatever you entered is not an integer. Try again.')
            else:
                print(f"Starting bankroll: {self.total}")

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total

    def take_bet(self):
        self.bet = None
        while not isinstance(self.bet, int):
            try:
                my_bet = input(f"What is your bet? (Chips: {self.total}) > ")
                self.bet = int(my_bet)
                assert self.bet < self.total, f"You only have {self.total}!"
            except Exception as e:
                print("Must be integer! Try again.")
                self.bet = None
            else:
                print(f"You placed a bet of: {self.bet}")


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



def hit(deck, player):
    player.add_card(deck.deal())
    player.ace_adjust()

def hit_or_stand(deck, player, dealer, chips):
    global playing
    while True:
        x = input("\nHit me? (y/n) ")
        if x.lower() == 'y':
            hit(deck,player)
            show_some(player,dealer)
            if player.value > 21:
                player_bust(player, dealer, chips)
                show_all(player, dealer)
                playing = False
                break
            else:
                playing = True
                continue
        elif x.lower() == 'n':
            print("dealer turn")
            playing = False
            break
        else:
            print("Sorry, please try again")
            continue
        break

def show_some(player, dealer):
    global player_cont
    global dealer_cont
    global dealer_hidden
    player_cont = ''
    dealer_cont = ''
    dealer_hidden = ''

    for c in player.cards:
        player_cont += '\n' + str(c)

    print('\nPLAYER 1 (VALUE: {})\nCARDS: {}'.format(player.value, player_cont))

    for num, c in enumerate(dealer.cards):
        if num == 0:
            dealer_hidden += str(c)
        if num > 0:
            dealer_cont += '\n' + str(c)

    print('\nDEALER CARDS: {}'.format(dealer_cont))

def show_all(player, dealer):
    global dealer_all
    dealer_all = ''
    print('\nPLAYER 1 (VALUE: {})\nCARDS: {}'.format(player.value, player_cont))
    #remake dealer hand in new string...
    for num, c in enumerate(dealer.cards):
        if num > 0:
            dealer_all += '\n' + str(c)
    print('\nDEALER (VALUE: {})\nCARDS: {}\nHIDDEN: {}'.format(dealer.value, dealer_all, dealer_hidden))

def player_bust(player, dealer, player_chip):
    print("\nPLAYER LOSES!!!!!!!!")
    player_chip.lose_bet()
    print("Player has {}".format(player_chip.total))

def player_win(player, dealer, player_chip):
    print("\nPLAYER WINS!!!!")
    player_chip.win_bet()
    print("Player has {}".format(player_chip.total))

def dealer_win(player, dealer, player_chip):
    print('\nDEALER WINS!!!')
    player_chip.lose_bet()
    print("Player has {}".format(player_chip.total))

def dealer_bust(player, dealer, player_chip):
    print('\nDEALER LOSES!)')
    player_chip.win_bet()
    print("Player has {}".format(player_chip.total))

def push(player,dealer):
    print("\nPlayers tie.")

if __name__ == '__main__':
    print("Welcome to blackjack.py...hope this works! lol :)")
    player_chip = Chips()
    playing_deck = Deck()

    player_chip.take_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())

    player_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())

    # show_some(player_hand, dealer_hand)

    # while playing:
    #     #ASK PLAYER IF HIT, HIT UNTIL PLAYING IS FALSE
    #     hit_or_stand(playing_deck,player_hand,dealer_hand, player_chip)


    #      ##perhaps indent this even more....elif <= 21, run the win checks indented.
    #     if player_hand.value < 21:
    #         while dealer_hand.value <= 17:
    #             hit(playing_deck, dealer_hand)

    #             if dealer_hand.value > 21:
    #                 dealer_bust(player_hand,dealer_hand,player_chip)
    #                 show_all(player_hand,dealer_hand)
    #             elif dealer_hand.value < player_hand.value:
    #                 dealer_win(player_hand,dealer_hand,player_chip)
    #                 show_all(player_hand,dealer_hand)
    #             elif player_hand.value > dealer_hand.value:
    #                 player_win(player_hand,dealer_hand,player_chip)
    #                 show_all(player_hand,dealer_hand)
    #             else:
    #                 push(player_hand,dealer_hand)
    #                 show_all(player_hand,dealer_hand)

    #     elif player_hand.value == 21:
    #         ##if len(player_hand.cont == 2, then it's a natural blackjack, and you can automatifcally win 1.5x on bet
    #         #let's try to not consider this right now lol....let's just get the game going)
    #         while dealer_hand.value <= 17:
    #             hit(playing_deck, dealer_hand)
    #             if dealer_hand.value != 21:
    #                 dealer_bust(player_hand, dealer_hand, player_chip)
    #                 show_all(player_hand,dealer_hand)
    #             else:
    #                 print("Dealer Hand Len: {}".format(len(dealer_hand.cont)))
    #                 print("Player Hand Len: {}".format(len(player_hand.cont)))
    # new_game = input("Play again? y/n: ")

    # if new_game.lower() == 'y':
    #     playing = True
    #     continue
    # if new_game.lower() == 'n':
    #     print("See you soon!")
    #     break


