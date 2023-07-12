logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import os
bids={}
def find_highest_bidder(bid_record):
    highest_bid=0
    winner = ""
    for bidder in bid_record:
        if highest_bid < bid_record[bidder]:
            highest_bid = bid_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        

bidding_finished = False

while not bidding_finished:
    name = input("What is your name ?\n")
    price = int(input("What is your bid? $\n"))
    bids[name] = price
    other_bids = input("Are there any other bids? 'yes' or 'no' \n")
    if other_bids == "no":
        bidding_finished = True
        find_highest_bidder(bid_record=bids)
    elif other_bids == "yes":
        input("press enter to clear terminal")
        os.system('cls')
