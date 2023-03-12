# %%
import heapq as hq

class Dijkstra:
    # Class variable
    # pi = 3.14
    # Initializing the list to be used in priority queue
    Q = []

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node

    # Initializing a node list with start node
    def initializeNodeList(self):
        # creating a tuple with cost to come, node index, parent node index = 0, and coordinate values (x,y)
        Dijkstra.Q.append(self.start_node)
        print('Initialized node list: ', Dijkstra.Q)

        return Dijkstra.Q
    
    def pushNode2List(self, Q, new_node):
        # using heapify to convert list into heap
        hq.heapify(Q)
        # using heappush() to push elements into heap
        hq.heappush(Q, new_node)
        print("List, after pushing new node to the queue ", Q)
        
        return list(Q)    

    # Method for updatig a node in list via heapq
    def updateNodeList(self, Q, node_idx, new_node):
        # using heapify to convert list into heap
        hq.heapify(Q)

        # creating a tuple with cost to come, node index, parent node index = 0, and coordinate values (x,y)
        x, y = node_idx

        # Updating a node in the list
        for i in range(len(Q)):
            if Q[i][3] == (x,y):
                Q[i] = new_node
        
        print("List, after updating node ",Q)

        return list(Q)

    
    def popMinNodefrmList(self, Q):
        # using heapify to convert list into heap
        hq.heapify(Q)
        # Push elements to the queue
        min_node = hq.heappop(Q)
        print("Minimum Node in the  list: ", min_node)
        print("Updated List: ", list(Q))

        return min_node, list(Q)
# %%
# initialize node
c = Dijkstra((0, 0, 0, (6,6)), (100, 100, 0, (200,600)))
nodesQueue = c.initializeNodeList()

# %%
# push a node to the list
new_node1 = (10, 1, 0, (10,10))
nodesQueue = c.pushNode2List(nodesQueue, new_node1)

# %%
# push another node to the list
new_node2 = (50, 2, 0, (20,20))
nodesQueue = c.pushNode2List(nodesQueue, new_node2)

# %%
#  update a particular node in the e list
updated_node = (0, 3, 0, (6,6)) # new node1 is modified on index
nodesQueue = c.updateNodeList(nodesQueue, (6,6), updated_node)
minimum_node, nodesQueue = c.popMinNodefrmList(nodesQueue)

# %%
