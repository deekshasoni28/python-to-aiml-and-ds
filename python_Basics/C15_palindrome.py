n=int(input("Enter a Number : "))
temp=n
rev=digit=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10

if(temp==rev):
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")
   
