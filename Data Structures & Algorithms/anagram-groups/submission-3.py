class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#01200... -> cat, act
        map = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] +=1
            map[tuple(count)].append(str)
        output = []
        for val in map.values():
            output.append(val)
        return output
