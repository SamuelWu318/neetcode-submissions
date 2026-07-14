class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        if len(nums) == 2: return [0, 1]

        for i in range(len(nums)):
            req = target - nums[i]

            if hash_table.get(req) is not None:
                if i > hash_table[req][0]:
                    return [hash_table[req][0], i]
                else:
                    return [i, hash_table[req][0]]

            if hash_table.get(nums[i]) is None:
                hash_table[nums[i]] = [i]
            else:
                hash_table[nums[i]].append(i)
        