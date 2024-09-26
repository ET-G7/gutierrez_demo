purchase1 = float(input("Enter amount of your first purchase: "))
purchase2 = float(input("Enter amount of your second purchase: " ))
purchase3 = float(input("Enter amount of your third purchase: "))

# Total Cost
totalcost = purchase1 + purchase2 + purchase3
print("Total Purchased: ", totalcost, " PHP")

# Discount
if totalcost > 100.00:
    print("You are qualified for a discount.")
    pre_discount = totalcost * 0.10
    discount = totalcost - pre_discount
    print("New total: ", discount, " PHP")
else:
    print("You are not qualified for discount")
    
# Loyalty Points
loyaltypoints = totalcost/10
print("Loyalty Points Earned: ", loyaltypoints)

# Payment
payment = float(input("Enter your payment: "))
totalcost = discount

if payment < totalcost:
    print("Payment Failed.")
else:
    print("Payment Successful.")
    print("Change: ", payment - totalcost)