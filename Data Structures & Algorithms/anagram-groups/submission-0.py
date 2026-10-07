class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:



#hashmap
#key- value;
#[0,0,0,0,...,0] (26x)  <- letters (key)
#string, string, string (value)

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()
