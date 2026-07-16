class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(1, len(numbers) + 1):
            needed = target - numbers[i - 1]
            
            if hash_map.get(needed) is not None:
                return [hash_map[needed], i]
            else:
                hash_map[numbers[i - 1]] = i


