class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for string in strs:
            count = "".join(sorted(string))
            if hash_table.get(count) is not None:
                hash_table[count].append(string)
            else:
                hash_table[count] = [string]
                
        return list(hash_table.values())