#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def kargerMinCut(Data):
    """
    This is the sample code of Karger's minimum cut problem
    
    Input: List representing graph structure 
    ex: [[1,2,3,4,7],[2,1,3,4],[3,1,2,4],[4,1,2,3,5],[5,4,6,7,8],[6,5,7,8],[7,1,5,6,8],[8,5,6,7]]
    
    Output: Minimum cut and final graph structure
    ex: (4, [[4, 7, 7, 7, 7], [7, 4, 4, 4, 4]])
    
    random_node: randomly selected node to merge other
    merged_node: select node that initially connects with random_node but get merged into random node"""
    
    #If input contains only two nodes, mission complete, return minimum cut and the graph list
    if len(Data) == 2:
        return len(Data[0]) - 1,Data
    else: 
        #Randomly select a starting node index and merged node index
        random_node_index  = random.randint(0,len(Data)-1)
        random_merge_index = random.randint(1,len(Data[random_node_index])-1)
        
        #Get the node number by selected index above
        random_node = Data[random_node_index][0]
        merged_node = Data[random_node_index][random_merge_index]
        
        #Iterate through the the list to update current graph after merger
        for i in range(len(Data)):
            #If we visit the node being merged, memorize the index and remove the random_node in that list
            if Data[i][0] == merged_node:
                merge_node_index = i
                Data[i] = [ x for x in Data[i] if x != random_node]
            #If we visit node except the selected random node, replace merged node with random node
            elif Data[i][0] != random_node:
                Data[i] = [ x if x != merged_node else random_node for x in Data[i]]    
        
        #Deal with random node
        #Remove merged node in the list of random node
        Data[random_node_index] = [x for x in Data[random_node_index] if x != merged_node]
        
        #Combine random node list with merged node list(except the first element which is the merged node)
        Data[random_node_index] = Data[random_node_index] + Data[merge_node_index][1:]
        
        #Remove list for merged node
        Data.remove(Data[merge_node_index])
        
    #Continuous recursion until only two nodes are left
    return kargerMinCut(Data)


# In[ ]:


testcase=[[1,2,3,4,7],[2,1,3,4],[3,1,2,4],[4,1,2,3,5],[5,4,6,7,8],[6,5,7,8],[7,1,5,6,8],[8,5,6,7]]
kargerMinCut(testcase)

