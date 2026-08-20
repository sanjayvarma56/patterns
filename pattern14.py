#Program to print numbers continously in a right angled triangle (Floyd's Triangle)
n=int(input("Enter the number of rows: "))
num = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(num,end=" ")
        num += 1
    print()
