N=int(input("enter the number"))
n=N
rev=0
while(N>0):
    R=N%10
    rev=rev*10+R
    N=N//10
if(n==rev):
    print("palindrom number")
else:
        print("this is not palindrom")