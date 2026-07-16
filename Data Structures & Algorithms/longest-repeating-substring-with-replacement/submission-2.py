class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l = 0
        most_freq = 0
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            most_freq = max(most_freq, hash_map[s[i]])

            if (i + 1 - l) - most_freq > k:
                hash_map[s[l]] -= 1
                l += 1
        
        return i + 1 - l