bid_list = [int(i) for i in input("Enter All Bid : ").split(" ")]
max_bid = max(bid_list)
count = bid_list.count(max_bid)
if len(bid_list) == 1:
    print("not enough bidder")
elif count > 1:
    print("error : have more than one highest bid")
else:
    bid_list.remove(max_bid)
    second = max(bid_list)
    print(f"winner bid is {max_bid} need to pay {second}")