amt=int(input("enter amount: "))
if(amt>25000):
    #print("You are our gold category customer")
    x=(amt-(amt*20)/100)
    print(f"You are our gold category customer and the amount to be paid: {x}")
elif(amt>10000 and amt<=25000):
    #print("You are our silver category customer")
    y=(amt-(amt*10)/100)
    print(f"You are our silver category customer and the amount to be paid: {y}")
elif(amt<=10000):
    #print("You are our bronze category customer")
    z=(amt-(amt*5)/100)
    print(f"You are our bronze category customer and the amount to be paid: {z}")