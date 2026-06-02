#1.Square Star Pattern
#2.Ask the user to enter a number.
#3.Use the outer loop to control the number of rows.
#4.Use the inner loop to control the number of columns.
#5.Print a star (*) in each column.
#6.Use end=" " to print stars on the same line.
#7.After printing all stars in a row,
#move to the next line using print().
#8.Repeat until a square pattern of size n × n is formed.

n= int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()

#OR

class pattern:
    def square_star_pattern(self,n):
        for i in range(0,n):
            for j in range(0,n):
                print("*",end=" ")
            print()
s = pattern()
s.square_star_pattern(n)