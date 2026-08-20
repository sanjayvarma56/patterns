#Program to print odd number of stars in diamond shape
#Program to print stars in diamond shape
n=int(input("Enter the number of rows: "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
for j in range(n-1,0,-1):
    print(" "*(n-j) + "*"*(2*j-1))

#Program to print stars in diamond shape using function
def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))
    for j in range(n-1,0,-1):
        print(" "*(n-j) + "*"*(2*j-1))

pyramid(5)