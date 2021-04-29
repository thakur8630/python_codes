class Table:
    def two(self):
        n=int(input("enter the number to the Table"))
        for i in range(1,11):
            print(n*i,end=" ")

obj=Table()
obj.two()