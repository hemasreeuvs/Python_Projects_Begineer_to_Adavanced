

bids= {}


continue_bidding = True


def find_highest_bidder(bidding_dict):
    highest_bid = 0

    for bidder in bidding_dict:
        bid_amt = bidding_dict[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The inner is {winner} with a bid of ${highest_bid}")

while continue_bidding:
    name = input(" What is your name?\n")
    price = int(input("Enter the Bid number? :\n"))
    bids[name]= price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

