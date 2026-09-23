
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:

#Input: nums = [1,2,3,1]

#Output: true

nums = [1,2,3,1]
#       0 1 2 3
for numbers in nums:
    if nums.count(numbers)>1:
        print(True)
        break
else:
    print(False)   

#Explanation:

#The element 1 occurs at the indices 0 and 3.

#Example 2:

#Input: nums = [1,2,3,4]

nums= [1,2,3,4]
for numbers in nums:
    if nums.count(numbers)>1:
        print(True)
        break
else:
    print(False)    

#Output: false

#Explanation:

#All elements are distinct.

#Example 3:

#Input: nums = [1,1,1,3,3,4,3,2,4,2]

nums = [1,1,1,3,3,4,3,2,4,2]
for numbers in nums:
    if nums.count(numbers)>1:
        print(True)
        break
else:
    print(False)    

#Output: true

 



