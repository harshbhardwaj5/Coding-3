class Solution:
    def groupAnagrams(self, strs):
        dic={}
        for i in strs:
            k=i 
            k=''.join(sorted(k))
            if k not in dic:
                dic[k]=[i]
            else:
                dic[k]+=[i]
        ls=[]
        for i in dic:
            ls.append(dic[i])
        return ls
s=Solution()
print(s.groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))