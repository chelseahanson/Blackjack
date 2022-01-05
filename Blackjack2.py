import random



# [win, tie, loss]

record = [0, 0, 0]



def keep_going(chips, record, retries = 4, complaint="Yes or no, please!"):

    print("Your record is", record[0], "wins,", record[1], "ties, and", record[2], "losses.")

    if chips == 0:

        return False

    while True:

        print("You have", chips, "chips.")

        ok = input("Would you like to play another hand? ")

        if ok in ('y', 'ye', 'yes'):

            return True

        if ok in ('n', 'no', 'nop', 'nope'):

            return False

        retries -= 1

        if retries < 0:

            raise IOError('uncooperative user')

            print(complaint)

        

def place_bet(prompt, chips, complaint="You don't have that many chips"):

    while True:

        bet = int(input(prompt))

        if bet <= chips:

            return bet

        if bet > chips:

            print(complaint)



def hit_or_stand(prompt, points, retries = 4, complaint="Enter 'hit' or 'stand'"):

    while True:

        print("You are sitting on a", points)

        choice = input(prompt)

        if choice in ('h', 'hi', 'hit'):

            return 'hit'

        if choice in ('s', 'st', 'sta', 'stan', 'stand', 'stay'):

            return 'stand'

        retries -= 1

        if retries < 0:

            raise IOError('uncooperative user')

            print(complaint)



def build_stack(decks):

    single_suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    single_deck = []

    for s in range(4):

        for i in single_suit:

            if i == 'A':

                v = 11

            if i == '2':

                v = 2

            if i == '3':

                v = 3

            if i == '4':

                v = 4

            if i == '5':

                v = 5

            if i == '6':

                v = 6

            if i == '7':

                v = 7

            if i == '8':

                v = 8

            if i == '9':

                v = 9

            if i == '10' or i == 'K' or i == 'Q' or i == 'J':

                v = 10      

            single_deck.append((i, v))

    stack = single_deck * decks

    return stack



def shuffle(stack):

    total = len(stack)

    for p in range(3):

        stack2 = []

        count = 0

        while len(stack) > 3:

            for card in stack:

                if count % 3 == 0:

                    stack2.append(card)

                elif count % 3 == 1:

                    stack2.insert(0, card)

                else:

                    stack2.append(card)

                stack.remove(card)

                count += 1

        stack = stack2

        stack2.clear

    return stack2



def hand_total(hand):

    total = 0

    for i in range(0, len(hand)):

        total += hand[i][1]

    if total > 21:

        for m in range(0, len(hand)):

            if hand[m][0] == 'A':

                total -=10

    return total



def display_deal(player, dealer):

    print(" Your Hand       Dealer's Hand")

    playerHand = "[ " + player[0][0] + " ][ " + player[1][0] + " ]"

    dealerHand = "[   ][ " + dealer[1][0] + " ]"

    print(playerHand, "     ", dealerHand)    

    return None



def display_hand(player):

    hand = ""

    for card in range(len(player)):

        hand += "[ " + player[card][0] + " ]"

    return hand



def play_hand(bet, chips, cards):

    # Empty hands before deal

    player_hand = []

    dealer_hand = []



    draw = 0;

    # Deal two cards each

    player_hand.append(cards[draw])

    draw = draw + 1

    dealer_hand.append(cards[draw])

    draw = draw + 1

    player_hand.append(cards[draw])

    draw = draw + 1

    dealer_hand.append(cards[draw])

    draw = draw + 1



    display_deal(player_hand, dealer_hand)



    # User plays hand

    player_total = hand_total(player_hand)

    

    while player_total < 21:

        p = hit_or_stand("Do you wan't to hit (take another card) or stand (end your turn)? ", player_total)

        if p == 'hit':

            player_hand.append(cards[draw])

            draw = draw + 1

            player_total = hand_total(player_hand)

            print(display_hand(player_hand))

            continue

        if p == 'stand':

            break

    if player_total > 21:

        print("Sorry, you went over 21! You lose your bet of", bet, "chips!")

        record[2] += 1

        chips -= bet

    else:

        # Dealer's hand is played

        dealer_total = hand_total(dealer_hand)       

        while dealer_total < 17:

            dealer_hand.append(cards[draw])

            draw = draw + 1

            dealer_total = hand_total(dealer_hand)



        print(display_hand(player_hand), "     ", display_hand(dealer_hand))

        

        if player_total == 21:

            print("Blackjack!")

            if dealer_total == 21:

                print("Unfortunately, the dealer got blackjack as well, your bet of", bet, "is refunded.")

                record[1] += 1

            else:

                print("You beat the dealer and won", bet, "more chips!")

                record[0] += 1

                chips += bet

        elif player_total < 21:

            if player_total > dealer_total or dealer_total > 21:

                print("You beat the dealer and won", bet, "more chips!")

                record[0] +=1

                chips += bet

            elif player_total < dealer_total:

                print("The dealer beat you with a", dealer_total,"and you lose your bet of", bet, "chips.")

                record[2] +=1

                chips -= bet

            elif player_total == dealer_total:

                print("This hand is a draw. Your bet of", bet, "is refunded.")

                record[1] += 1



    return chips, draw, record


def double_or_nothing(chips):
    
    print("DOUBLE OR NOTHING!")
    
    ok = input("Do you want to risk it all in double or nothing?")
    
    if ok in ('y', 'ye', 'yes'):

        return True

    if ok in ('n', 'no', 'nop', 'nope'):

        return False


def play_high_risk(bet, chips, cards):

    # Empty hands before deal

    player_hand = []

    dealer_hand = []



    draw = 0;

    # Deal two cards each

    player_hand.append(cards[draw])

    draw = draw + 1

    dealer_hand.append(cards[draw])

    draw = draw + 1

    player_hand.append(cards[draw])

    draw = draw + 1

    dealer_hand.append(cards[draw])

    draw = draw + 1



    display_deal(player_hand, dealer_hand)



    # User plays hand

    player_total = hand_total(player_hand)

    

    while player_total < 21:

        p = hit_or_stand("Do you wan't to hit (take another card) or stand (end your turn)? ", player_total)

        if p == 'hit':

            player_hand.append(cards[draw])

            draw = draw + 1

            player_total = hand_total(player_hand)

            print(display_hand(player_hand))

            continue

        elif p == 'stand':

            break
        
        else:
            continue
        

    if player_total > 21:

        print("Sorry, you went over 21! You lose all of your chips!")

        record[2] += 1

        chips -= bet

    else:

        # Dealer's hand is played

        dealer_total = hand_total(dealer_hand)       

        while dealer_total < 17:

            dealer_hand.append(cards[draw])

            draw = draw + 1

            dealer_total = hand_total(dealer_hand)



        print(display_hand(player_hand), "     ", display_hand(dealer_hand))

        

        if player_total == 21:

            print("Blackjack!")

            if dealer_total == 21:

                print("Unfortunately, the dealer got blackjack as well, you lose all of your chips.")

                record[1] += 1
                chips -= bet

            else:

                print("You beat the dealer and doubled your chips!")

                record[0] += 1

                chips += bet

        elif player_total < 21:

            if player_total > dealer_total or dealer_total > 21:

                print("You beat the dealer and doubled your chips!")

                record[0] +=1

                chips += bet

            elif player_total < dealer_total:

                print("The dealer beat you with a", dealer_total,"and you lose all of your chips.")

                record[2] +=1

                chips -= bet

            elif player_total == dealer_total:

                print("This hand is a draw. You lose all of your chips.")

                record[1] += 1

    return chips, draw, record
  

def main():

    print("Welcome to the Blackjack table!")

    chips = int(input("How many chips are you starting with? "))

    decks = int(input("How many decks would you like to play with? "))

    still_playing = True



    stack = build_stack(decks)

    current_stack = shuffle(stack)

    

    while still_playing:

        bet = place_bet("Please place your bet: ", chips)

        chips, cards_used, record = play_hand(bet, chips, current_stack)



        current_stack = current_stack[cards_used:]



        if len(current_stack) < decks * 13:
            
            if double_or_nothing(chips):
                
                bet = chips
                
                chips, cards_used, record = play_high_risk(bet, chips, current_stack)
                
                print("\nYou lost it all in high stakes!")
                
                print("\nYour record is", record[0], "wins,", record[1], "ties, and", record[2], "losses.")
                
                print("\nSee you next time!")
                
                return None
                

            print("\nPlease wait while we shuffle the cards\n")

            cards_used = 0

            stack = build_stack(decks)

            current_stack = shuffle(stack)

            

        still_playing = keep_going(chips, record)

    print("You leave with", chips, "chips!\nSee you next time.")

    return None



if __name__ == "__main__":

    main()
    