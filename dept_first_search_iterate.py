# Iterative solution
# O(v + e) - time, O(v) -> worst case

def dfs_iterative(graph, start):

    # Initializing variables, initial value in stack is "start"
    stack, path = [start], []

    # Loop trough stack, when node has been visited it was pop-ed from stack
    while stack:
        vertex = stack.pop()

        # If it is path mean that that vertice has been visited
        if vertex in path:
            continue

        path.append(vertex)

        # Adding neighbors to check
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

