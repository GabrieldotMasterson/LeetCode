class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max( len(word1), len(word2) ) ) :
            print(i)
            if len(word1)-1 >= i:
                merged.append(word1[i])
            if len(word2)-1 >= i:
                merged.append(word2[i])
        return "".join(merged)
