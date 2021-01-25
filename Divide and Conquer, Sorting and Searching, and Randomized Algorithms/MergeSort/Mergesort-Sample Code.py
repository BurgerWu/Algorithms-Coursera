#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mergesort(List):
    if len(List) == 1:
        return [0,List]
    else:
        div = len(List) // 2
        left_divide = mergesort(List[:div])
        right_divide = mergesort(List[div:])
        
        left_list = left_divide[1];
        right_list = right_divide[1];
        combined_list = list()
        i,j,count = 0,0,0
        for k in range(len(List)):
            if i + 1 > len(left_list):
                combined_list.append(right_list[j])
                j += 1
            elif j + 1 > len(right_list) or left_list[i] < right_list[j]:
                combined_list.append(left_list[i])
                i += 1
            else:
                combined_list.append(right_list[j])
                j += 1
                count = count + len(left_list) - i
        return [left_divide[0] + right_divide[0] + count, combined_list]
    

