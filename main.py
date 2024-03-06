from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
blind_auction = {}

run_auction = True
while run_auction:
    name = input("What is your name?\n")
    bid = int(input(f"How much do you want to bid, {name}?\n$"))
    blind_auction[name] = bid
    more_bidders = input("Does anyone else want to bid? Type yes, otherwise type no. \n")
    if more_bidders == "yes":
        clear()
    elif more_bidders == "no":
        run_auction = False

highest_bidder = ""
highest_bid = 0
for bidder, bid in blind_auction.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
