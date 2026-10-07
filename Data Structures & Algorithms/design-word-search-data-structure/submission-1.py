class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    #if encounter ., then we check all current children of curr, do recursive call here,
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            return cur.endOfWord
        return dfs(0, self.root)

                
            #set up
            #dfs:
            #base case -- if sucess ; if failure
            #do the work for current node
            #recursive call to next node
            #return result
        
