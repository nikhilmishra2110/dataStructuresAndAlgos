def findNumbers(nums):
    res = 0
    for num in nums:
        if len(str(num)) % 2 ==0:
            res +=1
    return res

print(findNumbers([1234,124,6758,567,675755565]))