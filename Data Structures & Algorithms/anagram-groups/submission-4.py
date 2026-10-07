class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array : "act", "cat", "hat"
        map = {}
        res = []
        for s in strs:
            temp = [0] *26
            for c in s:
                temp[ord(c) - ord("a")] +=1
            key = tuple(temp)
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]
        return list(map.values())
            

                


