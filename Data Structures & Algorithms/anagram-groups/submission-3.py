class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_array = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freq_array[tuple(count)].append(s)
        return list(freq_array.values())