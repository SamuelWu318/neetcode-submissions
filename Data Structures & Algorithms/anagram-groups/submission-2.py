class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for string in strs:
            count = "".join(sorted(string))
            hash_table[count].append(string)
                
        return list(hash_table.values())