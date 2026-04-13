n=int(input("Enter a number: "))
temp=n
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print(f"sum of digits in {temp} is {total}")    