#!/usr/bin/python3

import sys

if len(sys.argv) <= 1:
    print("Please provide a target sum number")
    quit()

def slow_canSum(arr, target):
    if target == 0:
        return True
    if target < 0:
        return False

    for n in arr:
        #for every number in the array
        comp = target - n
        if canSum(arr, comp) == True:
            return True

    return False

def canSum(arr, target, hmap = {}):
    if target in hmap:
        return hmap[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for n in arr:
        #for every number in the array
        comp = target - n
        if canSum(arr, comp) == True:
            hmap[comp] = True
            return hmap[comp] 

    hmap[comp] = False
    return hmap[comp] 



print("Given a targetSum and an array of integers determine if the numbers in the list can sum upto the target.\n")

nums = [4,2,9,1,3,8,5]
print(f"The list is {nums} and the target is {sys.argv[1]}")
#print(canSum(nums, int(sys.argv[1])))
target = sys.argv[1]
target = int(target)
print(canSum(nums, target))
