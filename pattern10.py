#Inverted Number Pattern in sequence and no repetition in row
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Inverted Number Pattern in sequence and repetition in row
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    