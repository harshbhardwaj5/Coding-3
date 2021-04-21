    for i, x in enumerate(nums):
            print(i)
            if target - x in numMap:
            
                return [numMap[target-x], i]
            
            numMap[x] = i