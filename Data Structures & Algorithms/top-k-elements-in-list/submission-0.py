class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        for key, value in hash_map.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


            