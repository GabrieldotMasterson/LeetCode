class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        if s != "":
            for i in t:
                if counter < len(s):
                    if i == s[counter]:
                        counter += 1
                else: break


        return True if counter >= len(s) else False

        