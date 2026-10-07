class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       sLetters = {}
       tLetters = {}
       if len(s) != len(t):
        return False
       for letter in s:
        sLetters[letter] = sLetters.get(letter,0) +1
       for letter in t:
        tLetters[letter] = tLetters.get(letter,0) +1
       if sLetters == tLetters:
        return True
       else:
        return False 