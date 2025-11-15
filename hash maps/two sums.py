# nums = [7,9,8,5]
# for i, n in enumerate(nums):
#     print(i,n)

shm = {
    
}

# if "a" in shm:
#     print(1)


# shm[2] = 1
# print(shm)

# if 2 in shm:
#     print(1)

class Solution:
    def twoSum(self, nums, target: int):
        hm = {} # value: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hm:
                return [hm[diff], i]
            hm[n] = i
        return []