#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Example 2:
nums = [0,1,0,3,12]
count=0
for numbers in nums:
    if numbers==0:
        count=count+1
empty_list=[]
for numbers in nums:
    if numbers!=0: 
        empty_list.append(numbers)
for i in range(count):
    empty_list.append(0)
print(empty_list)    
        

#Input: nums = [0]
#Output: [0]
nums = [0]
count=0
for numbers in nums:
    if numbers==0:
        count=count+1
empty_list=[]
for numbers in nums:
    if numbers!=0: 
        empty_list.append(numbers)
for i in range(count):
    empty_list.append(0)
print(empty_list)  



