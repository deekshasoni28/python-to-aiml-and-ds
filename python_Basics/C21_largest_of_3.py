a,b,c=map(int,input("Enter three Numbers: ").split())
if(a>=b and a>=c):
    print(f'{a} is largest')
elif(b>=a and b>=c):
    print(f'{b} is largest')
else:
    print(f'{c} is largest')
  
