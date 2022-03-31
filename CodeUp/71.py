# 깊이 우선 탐색
graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}
print(graph)
def dfs(graph, start):
    visited = []
    stack = [start]
    

    while stack:
        n = stack.pop()
        print(n)
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            print('stack',stack)
            print('viseted ',visited)
    return visited

print(dfs(graph, 'E'))