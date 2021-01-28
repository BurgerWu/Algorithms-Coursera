#!/usr/bin/env python
# coding: utf-8

# In[17]:


def quicksort(List, pivot_type = "median"):
    #Firstly, retrieve number of elements in the list
    l = len(List)
    
    #Check pivot_type status, and swap the pivot to first element per the instruction
    #Check if pivot_type is median 
    if pivot_type.strip().lower()=="median":
        if l <= 1:
            return [A,0]
        else:
            middle = int((l-1) // 2)       
            if List[-1]>List[middle]>List[0] or List[-1]<List[middle]<List[0]:
                List[0], List[middle] = List[middle], List[0]
            
            elif List[middle]>List[-1]>List[0] or List[middle]<List[-1]<List[0]:
                List[0], List[-1] = List[-1], List[0]
            
    #Check if pivot_type is last        
    elif pivot_type.strip().lower()=="last":
        List[0], List[-1] = List[-1], List[0]
        
    #Check if pivot_type is first    
    elif pivot_type.strip().lower() == "first":
        List[0] = List[0]
        
    #Output error message if pivot_type input can not be identified    
    else:
        print("pivot_type error!!") 
    
    #Define first element as pivot,idx to track element less than pivot and n for indexing element 
    pivot=List[0]
    idx=1
    n=1
    
    while n<=l-1:
        #If the element is greater than pivot, simply add 1 to n
        if List[n] > pivot:
            n+=1
        #If the element is less than pivot, swap element with idx (last element greater than pivot)
        else:
            List[n], List[idx] = List[idx], List[n]
            idx += 1
            n += 1
    #swap pivot with the element less than pivot in left right boundary
    List[0],List[idx-1] = List[idx-1],List[0]
    
    #Further recurse the sorting algorithm on left side
    if len(List[:idx-1]) > 1:
        List[:idx-1],l1 = quicksort(List[:idx-1],pivot_type)
    else:
        l1 = 0
        
    #Further recurse the sorting algorithm on right side    
    if len(List[idx:])>1:
        List[idx:],l2=quicksort(List[idx:],pivot_type)
    else:
        l2 = 0
    
    #Compute total number of comparison
    total = l-1+l1+l2
    
    return List,total

