#To print pyramid pattern to print fixed digit in every row
n = int(input("Enter the number of Rows:"))
for i in range(n):
    print((" "*(n-i-1))+ (str(i+1)+" ")*(i+1))