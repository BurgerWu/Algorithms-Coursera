def dijkstra(edgedist, start):
    """
    This function applies Dijkstra algorithms to compute shortest path from starting points to rest of the pointd.
    
    Input: 
    edgelist: Defines distance between each nodes
    start: Starting point of the algorithm
    
    Output:
    dist: Distance from starting point to rest of the nodes
    visited: Sequence of nodes visited    
    """
    #Define a large distance for unvisited nodes
    dist = [1000000] * (len(edgedist) + 1)
    
    #Define index as starting node number
    index = start
    
    #Initialize starting point distance and visited list
    dist[start] = 0
    visited = []
    
    #Continue if there is still node unvisited
    while len(visited) < len(edgedist):

        #Iterate through all neighbor nodes connected with present indexed node
        for i in list(edgedist[index].keys()):   
            
            #Compare the distance value of original distance of neighbor node and the distance of present node plus 
            #distance between these two nodes. If the later is smaller, update the distance of neighbor node in 
            #distance list.
            if dist[i] > dist[index] + edgedist[index][i]:
                dist[i] = dist[index] + edgedist[index][i]        
        
        #Append present node to visited list
        visited.append(index)
        
        #Calculate minimum distance of unvisited nodes
        dist_unvisited = [dist[x] for x in edgedist.keys() if x not in visited]
        
        #If the dist_unvisited list is empty or full of initial extreme values, it means that all nodes that can be 
        #visited  through start point have been already visited, thus end the while loop. Otherwise, we find the 
        #uvisited node with minimum distance and assign it as our next visited node.
        if len(dist_unvisited) == 0 or min(dist_unvisited) == 1000000:
            break
        else:
            index = [x for x in edgedist.keys() if dist[x] == min(dist_unvisited) and x not in visited][0]
        
    return dist,visited   
