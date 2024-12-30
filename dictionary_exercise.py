def compare_bids(bidders_dict):
    max = 0
    for bids in bidders_dict:
        if(bidders_dict[bids] > max):
            max = bidders_dict[bids]
            key_reqd = bids
    return max,key_reqd

bidders_info = {}

flag = False

enter = int(input("If you want to enter the bidding game press 1 else press 0"))

if enter == 1:    
    flag = True 
elif enter == 0:
    flag = False  

while flag is True:            
    print(f"~~~~~~~~~~~~~~------------WELCOME TO THE BID-----------~~~~~~~~~~~~~")
    name = input("Please enter your name: ")
    bid = int(input("Please enter the amount you would like to bid: "))
    bidders_info[name] = bid
    should_continue = input("Is there a next bidder? Enter yes or no: \n").lower()
    if should_continue == "yes":
        print("\n" * 50)
    elif should_continue == "no":
        flag = False

max_bid,key_req = compare_bids(bidders_info)
print(f"The max bid is by {key_req} of the amount: {bidders_info[key_req]}")      



    

        
        

