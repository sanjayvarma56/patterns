#Program to print stars in diamond shape
n=int(input("Enter the number of rows: "))
for i in range(n):
    print(" "*(n-i-1) + "* "*(i+1))
for j in range(n-1,0,-1):
    print(" "*(n-j) + "* "*j)

#Program to print stars in diamond shape using function
def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1) + "* "*(i+1))
    for j in range(n-1,0,-1):
        print(" "*(n-j) + "* "*j)

pyramid(5)