# while with else statement
# a=input("Enter a number")
a=8
i=1
c=0
while i<=a:
    if a%i==0:
        # print(1)
        c=c+1
    i=i+1
if c==2:
    print("prime")  
else:
    print("Composite")      