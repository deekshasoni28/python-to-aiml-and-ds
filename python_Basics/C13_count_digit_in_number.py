n=(input("enter a number:"))
temp=n
count=0
while(n>0):
    n=n//10
    count+=1
print(f"total digits in {temp} is {count}")   
