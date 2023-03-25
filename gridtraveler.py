#!/usr/bin/python3

def slow_traveler(m, n):
    #recursive function
    if (m == 0 or n == 0):
        return 0

    if (m == 1 and n == 1):
        return 1

    # m - 1 means go down (decrease rows) and if n - 1 then you goto right move a columns
    return slow_traveler(m - 1, n) + slow_traveler(m, n - 1)


def traveler(m, n, hmapa):
    store = str(m) + "," + str(n)
    if store in hmapa:
        return hmapa[store]
    if (m == 0 or n == 0):
        return 0

    if (m == 1 and n == 1):
        return 1

    hmapa[store] = traveler(m - 1 , n , hmapa) + traveler(m, n -1, hmapa)

    return hmapa[store]


print("We will calculate the total number of ways to travel through a m * n grid")
print("The traveler can go either down or right at a time where we start off at the top-left and make our way to bottom -right")
print("m -> number of rows \nn -> number of columns\n")

rows = input("Enter number of rows (m): ")
cols = input("Enter number of colums (n): ")

rows = int(rows)
cols = int(cols)

hmap = {}
print("Possible ways to go: "+ str(traveler(rows, cols, hmap)))
