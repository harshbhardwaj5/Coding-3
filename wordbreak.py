class Solution:

        def wordBreak(self, s, wordDict):
            starts = [0]
            for i in range(len(s)):
                for j in starts:
                    if s[j:i+1] in wordDict:  #j always zero  
                        starts.append(i+1)
                        break
            print(starts)
            return starts[-1] == len(s)

s=Solution()
s.wordBreak("leetcode", ["leet","code"])