import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Return a random card"""
    cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
    return random.choice(cards)

def start_game():
    player_cards = []
    computer_cards = []
    is_game0ver = False
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    
    while not is_game0ver:
        player_score = calculat_score(player_cards)
        computer_score = calculat_score(computer_cards)
        print(f"Your cards :{player_cards} , Current score : {player_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21 :
            is_game0ver = True
        else:
            player_should_deal = input("Type 'y' to get anthor card , Type 'n' to pass ")
            if player_should_deal == 'y' :
                player_cards.append(deal_card())
            else:
                is_game0ver = True  
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculat_score(computer_cards) 
    print(f"Your final hand : {player_cards} , final score : {player_score}")
    print(f"Computer's final hand : {computer_cards} , final score : {computer_score}")
    print(compare_score(player_score , computer_score))
def calculat_score(cards):
    """Take a list of cards and return the score of these"""
    count = 0
    for i in cards:
        count += i
    # Hand condition
    if sum(cards) == 21 and len(cards) == 2:
        #sum(cards) == 21 this means that one of them has ace  + 10
        return 0  
    if (11 in cards) and (sum(cards)>21):
        cards.remove(11)
        cards.append(1)
    return count   
# list slicing  => a[len(a):] = b   // same as a.extend(b)
def compare_score(player_score , computer_score):
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0 :
        return "Lose! , Has Black Jack"
    elif player_score == 0 :
        return "Win with a black jack"
    elif player_score > 21:
        return "You lose"
    elif computer_score > 21 :
        return "You win"
    elif player_score > computer_score :
        return "You win "
    else :
        return "You lose"
    

while input("Do you want to play Black Jack  ? 'y' or 'n' :") == 'y':
    start_game()
    if input("Enter y  to restart the game:") == 'y':
        os.system('cls')