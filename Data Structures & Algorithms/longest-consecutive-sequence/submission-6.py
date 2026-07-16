class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        total = 0

        for num in nums:
            if not hash_map[num]:
                hash_map[num] = hash_map[num - 1] + hash_map[num + 1] + 1
                hash_map[num - hash_map[num - 1]] = hash_map[num]
                hash_map[num + hash_map[num + 1]] = hash_map[num]
                total = max(total, hash_map[num])
        
        return total
