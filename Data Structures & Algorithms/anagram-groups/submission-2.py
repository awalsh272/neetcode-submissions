class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        anagram_map = {}
        for i, s in enumerate(sorted_strs):
            if s not in anagram_map:
                anagram_map[s] = [strs[i]]
            else:
                anagram_map[s].append(strs[i])
        return list(anagram_map.values())
    