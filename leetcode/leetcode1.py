hashtable = dict() #创建一个哈希表用字典
nums = [2,7,11,15]
target = 9
for i,num in enumerate(nums):
    if target-num in hashtable:
        print([hashtable[target-num],i])
    else:
        hashtable[num] = i
