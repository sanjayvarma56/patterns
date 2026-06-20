#To print pyramid pattern to print fixed digit in every row
n = int(input("Enter the number of Rows:"))
for i in range(n):
    print((" "*(n-i-1))+ (str(i+1)+" ")*(i+1))

#OR

#To print pyramid pattern to print fixed digit in every row
n= int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()