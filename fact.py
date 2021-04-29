class factorial:
    def fact(self):
        n=int(input("enter the number...."))
        if n<0:
            return 0
        elif n==0 or n==1:
            return 1
        else:
            facto=1
            while(n>1):
                facto*=n
                n-=1
                return facto
            
        

obj=factorial()
obj.fact()