
# 스택을 이용한 dfs

def itertive_dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)

            for w in graph[v]:
                stack.append(w)
    return discovered

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

print(itertive_dfs(1))
# [1, 4, 3, 5, 7, 6, 2]
# 역순 방문