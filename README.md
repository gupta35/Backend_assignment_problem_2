# Backend_assignment_problem_2
In this given problem we need to find the total number of epicentre node. To solve this problem here we use BFS algorithm.

## Description
In this given problem statement, we have the total number of nodes (n), the total number of hotspots(h), and the distance from the infected cities.
In the second line of input, we have the list of node names that are already hotspots.
First, we consider all the cities as the bidirectional graph node.
To find the total number of hotspots here, we use the BFS algorithm to find the minimum distance between the node.
Initial distance from the infected cities we assume as zero.
Then we implement a queue in which first we pop the current node "num" and add the distance of the adjacent non-visited node.
Follow the above process for all nodes.
The return value of this function is the distance between the current node and the hotspot node.
In the second function, we append all the edges for {u,v}.
We take input(n,h,x) from the user and split it into a list. 
In the second line of input h = len(hotspot_list). List of hotspots cities.
The next (n-1) line of input show the edge(Road) connection between the node.
Then we find the distance from each node to the hotspot(epicenter node) if this is less than or equal to the x. then we add this node to the epicenter node.
Finally, we get the updated list of epicenter nodes, and the output is the len(epicentre_node_list).

## Run the code
```python
python code.py
```

## Sample Input
```python
5 2 2
5 2
1 2
2 3
4 5
2 4
```

## Sample Output
```python
3
```
