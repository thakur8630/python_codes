N=int(input("enter the number"))
f=0    # to decrease the coloumn
for i in range(N):
    c=N
    for j in range(1,N*N+1-f):
        print(c,end=" ")
        if j%(N-i)==0:
            c=c-1
            f=f+N
            print("$",end=" ")
            print(" ")

