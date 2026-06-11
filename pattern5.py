#Reverse Incremental Number Triangle
n= int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()

#OR
class pattern:
    def reverse_incremental_number_triangle(self, n):
        for i in range(n, 0, -1):
            for j in range(0, i):
                print(j + 1, end=" ")
            print()
s = pattern()
s.reverse_incremental_number_triangle(4)
s.reverse_incremental_number_triangle(2)