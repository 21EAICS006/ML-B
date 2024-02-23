def IsPerfect(arr,n):
    rev = arr[::-1]
    if arr==rev:
        print("PERFECT")
    else:
        print("NOT PERFECT")
# arr = [20, 4, 15, 10, 14, 19, 11, 8, 5, 19, 13, 8, 18, 13, 3, 12, 8, 16, 19, 11]

arr = [15, 20, 5, 6,5, 6, 13, 4, 3, 4, 13, 6, 5, 6, 5, 20, 15]

IsPerfect(arr,17)
