from logo import logo
print(logo)

end_of_bids = False
bids = {}

def highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a big of £{highest_bid}")

while not end_of_bids:
    name = input("Enter name of bidder: ")
    price = int(input("Enter the bid price: "))
    bids[name] = price
    end_bids = input("Anymore bidders y/n: ")
    if end_bids == "n":
        end_of_bids = True
        highest_bidder(bids)

