class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_select in range(len(nums)):
            for num in range(len(nums)):
                if nums[num_select] + nums[num] == target and num_select != num:
                    return num_select, num
        