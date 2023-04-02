from collections import deque

"""
Pyton Deque is a double ended queue
q = deque()

has the methods:
append() add to the queue
popleft() pops the oldest member in the queue

appendleft() add to the queue but you now in the front of the queue
pop() removes the last member to join

for a FIFO data struct
use append and popleft()
append = you join the line
popleft = the person front of the line is served

for a LIFO data struct
use append and pop()
append = you join the line
pop = you are removed from the line

"""
def bfs(matrix, start):
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        curr = queue.popleft()
        print(curr)

        for node in matrix[curr]:
            queue.append(node)

def bfs_recur(matrix, start):
    print(start)

    for node in matrix[start]:
        bfs_recur(matrix, node)

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

print("Iterative: ")
bfs(graph, "a")
print("\nRecursive: ")
bfs_recur(graph, "a")