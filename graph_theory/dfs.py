def dfs(matrix, start):
    stack = []
    stack.append(start)

    while (len(stack) > 0):
        curr = stack.pop()
        print(curr)
        for node in graph[curr]:
            stack.append(node)

def dfs_recur(matrix, start):
    print(start)

    for node in matrix[start]:
        dfs_recur(matrix, node)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

print("Iterative: ")
dfs(graph, "a")
print("\nRecursive: ")
dfs_recur(graph, "a")

