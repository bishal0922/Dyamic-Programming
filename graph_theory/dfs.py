def dfs(matrix, start):
    stack = []
    stack.append(start)

    while (len(stack) > 0):
        curr = stack.pop()
        print(curr)
        for node in graph[curr]:
            stack.append(node)



graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

dfs(graph, "a")

