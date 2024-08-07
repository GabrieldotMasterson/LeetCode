
class Solution(object):
    def findClosestNumber(self, nums):
        nums_dist = [abs(x) for x in nums]
        if nums_dist.count(min(nums_dist)) >= 2 and len(set([x for x in nums if abs(nums_dist[nums.index(x)]) == abs(x)])) != 1:
            return min(nums_dist)
        else:
            return nums[nums_dist.index(min(nums_dist))]

        