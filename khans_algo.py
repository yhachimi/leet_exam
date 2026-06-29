from collections import deque

def topo_sort_kahn(graph):
    indegree = {node: 0 for node in graph}

    # build indegree
    for node in graph:
        for nei in graph[node]:
            indegree[nei] += 1

    # start with nodes that have no dependencies
    q = deque([node for node in graph if indegree[node] == 0])

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # cycle check
    if len(result) != len(graph):
        return []

    return result
