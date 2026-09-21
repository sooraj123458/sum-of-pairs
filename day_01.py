nums=[2,7,11,15]
target=9
for numbers in nums:
    difference=target-numbers
    if difference in nums:
        i=nums.index(numbers)
        j=nums.index(difference)
        print([i,j])
        break
