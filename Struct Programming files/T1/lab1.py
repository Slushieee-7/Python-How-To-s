oneLiterorLess = int(input("How many bottles have one liter or less: "))
moreThanOneLiter = int(input("How many bottles have more the one liter: "))
refund1 = oneLiterorLess * 0.10
refund2 = moreThanOneLiter * 0.25
totalRefund = refund1 + refund2

print("The refund for returning these containers is ", "$",totalRefund)