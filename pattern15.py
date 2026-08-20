#Program to print right angled trainagle using alphabets
n = int(input("Enter the number of rows: "))
for i in range(n):
    k = ord("A") + i
    for j in range(i+1):
        print(chr(k), end= " ")
        k = k + n - j - 1
    print()