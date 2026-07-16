class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l = 0
        most_freq = s[0]
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            if hash_map[s[i]] > hash_map.get(most_freq):
                most_freq = s[i]

            if (i + 1 - l) - hash_map[most_freq] > k:
                hash_map[s[l]] -= 1
                l += 1
        
        return i + 1 - l