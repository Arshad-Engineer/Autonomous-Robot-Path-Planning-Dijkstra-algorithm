# %%
import heapq as hq


# updatinga a node in heapq

# creeating a tuple with cost to come, node index, parent node index = 0, and coordinate values (x,y)

d1 = (34, 1, 0, (2,3))

d2 = (43, 2, 0, (4,5))

d3 = (23, 3, 0, (7,1))

# Initializing the list to be used in priority queue
Q = []
print('Initialized node list: ', Q)

# Push elements to the queue

hq.heappush(Q, d1)
hq.heappush(Q, d2)
hq.heappush(Q, d3)

print("List, after pushing elements to the queue ", Q)

hq.heapify(Q)
print("List, after heapify: ", Q)

# Updating a node in the list
for i in range(3):
    if Q[i][3] == (4,5):
        Q[i] = (20, 1, 0, (4,5))

hq.heapify(Q)
print("List, after modifying & heapify ",Q)

# %%



