n=int(input("Enter a Number : "))
temp=n
rev=digit=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(f"Reverse of {temp} : {rev}")

