n=(input("Enter a number : "))
temp=n
power=len(n)
n=int(n)
total=0
while(n>0):
    digit=n%10
    total=total+(digit**power)
    n=n//10

if(total==int(temp)):
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")    
