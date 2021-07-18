
## Dijkstra's Shortest Path Algorithm

- Provided with data containing distance information between nodes, we can use Dijkstras shortest path algorithm to calculate shortest path from starting point to remaining nodes. 

- Firstly, we will assign an extremely distance value for other nodes except starting point. Then we update the distance that has connection with our starting node. 

- Secondly, we choose the remaining node having least distance as our next node. At this point, it becomes a bit different from the starting point, we compare the initial distance with the distance of present node plus the distance between present node and neighbor node and leave whichever is less. After iterating through all the neighbor nodes, we comes back at the step of choosing unvisited node with least distance as our next node. 

- The termination of this iterating process is either all nodes are visited or there is no more connection when we start from the starting point.
