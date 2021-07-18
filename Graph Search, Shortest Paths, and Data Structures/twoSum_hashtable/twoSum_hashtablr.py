def twoSum(nums,target):
    """
    This function is twoSum with help of hashtable
    
    Input
    nums: numbers to be added
    target: numbers to see if numbers in nums can add up
    
    Output
    count: counts of numbers in target that can be added up by numbers in nums 
    """
    #Initialize count and hash table
    count=0
    hash_table={}
    
    #Build hashtable
    for i in range(len(nums)):    
        hash_table[nums[i]] = i
    
    #Iterate through targets and nums to see if corresponding numbers exist in hashtable
    for i in range(len(target)):
        for j in range(len(nums)):
            if target[i] - nums[j] in hash_table and nums[j] != target[i] - nums[j]:
                count += 1
                break
    return count
