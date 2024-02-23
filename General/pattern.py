n = int(input("Enter the number of rows: "))

print("Line 1: before the breakpoint")

for row in range(1,n+1):
    for col in range(1, row+1):
            print(col, end=" ")
    print("")

print("Line 2: After for loop")
