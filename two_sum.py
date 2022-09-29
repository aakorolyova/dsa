#  find indices of the two numbers in an array that add up to the target

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_id = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_id:
                return [i, num_to_id[diff]]
            num_to_id[num] = i            
            
