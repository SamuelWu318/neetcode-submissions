class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(num for num in nums))
        nums.sort()
        print(nums)

        total = 1
        max_nums = 1

        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                max_nums += 1
                total = max(total, max_nums)
            else:
                max_nums = 1
        
        return total
                
