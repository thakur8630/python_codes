class percentage:
    def profit():
        cost=int(input("enter the cost price..."))
        sell=int(input("enter the selling price..."))
        pro=sell-cost
        loss=cost-sell
        if(cost<sell):
            print("you are in profit",pro)
        else:
            print("you are in loss",loss)    
obj=percentage()
obj.profit()