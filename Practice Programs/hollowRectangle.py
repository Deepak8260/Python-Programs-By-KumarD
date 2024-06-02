r=int(input("Enter the no of rows: "))
c=int(input("Enter the no of columns: "))

if r==c or r==0 or c==0: 
    print("Please enter coreect no of rows and columns to become a rectangle")
else:
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1:
                print("*",end="  ")
            else:
                print(" ",end="  ")
            
        print()
            
        
    
    

        