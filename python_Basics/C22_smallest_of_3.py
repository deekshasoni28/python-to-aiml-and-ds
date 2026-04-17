a,b,c=map(int,input("Enter three Numbers: ").split())
if(a<=b and a<=c):
    print(f'{a} is smallest')
elif(b<=a and b<=c):
    print(f'{b} is smallest')
else:
    print(f'{c} is smallest')
