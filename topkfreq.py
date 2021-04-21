def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import OrderedDict
        dic={}
        ls=[]
        for i in nums:
            if i in dic:
                dic[i]+=1 
            else:
                dic[i]=1

                #extract elements with maximum frequency from dic
        while k != 0:
            max_key = max(dic, key=dic.get)
            ls.append(max_key)
            del dic [max_key]
            k-= 1
        return ls

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        ls=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        dic={k: dic[k] for k in sorted(dic, key=dic.get, reverse=True)}   #sort on basis of value
        print(dic)
        for i in dic.keys():         #iterate on basis of keys
            if k<=0:
               break
            ls.append(i)
            k-=1
        return ls
		