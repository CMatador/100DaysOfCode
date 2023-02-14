# Day 9 - Secret Auction

from day9art import logo
from replit import clear

print(logo)
auction_bids = {}
finished = False

print('Welcome to the secret auction program.')

while not finished:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))
    auction_bids[name] = bid
    more_bids = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    if more_bids == 'no':
        finished = True
        clear()
    else:
        clear()

highest_bidder = max(auction_bids, key=auction_bids.get)
print(f'The winner is {highest_bidder} with a bid of ${auction_bids[highest_bidder]}.')