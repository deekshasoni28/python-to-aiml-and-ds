n=int(input("Enter a NUmber:"))
a=0
b=1
c=0
if (n==1):
    print(a)
else:    
    print(a,b,end=" ")
    for i in range (0,n-2):
        c=a+b
        print(c, end=" ")
        a=b
        b=c
