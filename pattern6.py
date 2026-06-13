#(Repeated)Number Triangle Pattern
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()

#(Repeated) Number Triangle Pattern
n=int(input("Enter the number: ")) 
for i in range(0,n):
    for j in range(0,i+1):
        if (j<=i):
            print(i+1,end=" ")
    print()

#(Repeated) Number Triangle Pattern
n=int(input("Enter the number: ")) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()