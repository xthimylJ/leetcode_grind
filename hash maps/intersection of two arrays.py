# list1 = [1,2,3,3,5,5,6,6]
# set_list1 = set(list1)
# print(set_list1)


class Solution:
    """my initial solution. this has 20 ms runtime"""
    def intersection(self, nums1, nums2):
        intersections = []
        for i in set(nums1):
            if i in set(nums2):
                intersections.append(i)
        return intersections
    
    """this is from youtube. less than 5 ms runtime"""
    def intersection2(self, nums1, nums2):
        seen = set(nums1)
        intersections = []
        for i in nums2:
            if i in seen:
                intersections.append(i)
                seen.remove(i)
        return intersections
    

    