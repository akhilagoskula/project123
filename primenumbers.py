Prime number:

num = int(input("enter number:"))
for i in range(1,num+1):
     if num%i==0:
       print(num,"is not a prime")
       break
else:
    print(num,"is prime")