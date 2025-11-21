class Solution:

    # my first solution. Runtime: 8121 ms bruh
    def findDisappearedNumbers(self, nums):
        missing = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing.append(i)
        return missing
    
    # my second solution.
    def findDisappearedNumbers2(self, nums):
        setNums = set(range(1,len(nums)+1))
        for i in nums:
            if i in setNums:
                setNums.remove(i)

        nums = list(setNums)
        return nums
        


