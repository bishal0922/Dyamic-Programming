#!/usr/bin/python3

import sys
print("Today we are going to write a fibonacci function using dynamic programming")

hmapa = {}
def fib(n, hmap):
    if n in hmap: 
        return hmap[n]
    if n <= 2:
        return 1
    hmap[n] = fib(n-1, hmap) + fib(n-2, hmap)
    return hmap[n]

def slow_fib(n):
    if n <= 2:
        return 1
    return slow_fib(n-1) + slow_fib(n -2)

print(fib(int(sys.argv[1]), hmapa))

