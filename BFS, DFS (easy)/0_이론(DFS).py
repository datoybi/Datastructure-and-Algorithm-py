'''
DFS(Depth-First Search) : 깊이 우선 탐색 - Stack 사용

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
그 노드를 스택에 넣고 방문 처리를 합니다. 방문하지 않은 인접 노드가 없으면
스택에서 최상단 노드를 꺼냅니다.
3. 더이상 2번의 과정을 수행할 수 없을 떄까지 반복합니다.


호출을 한 그래프가 트리에서 부모이다.
DFS는 재귀, BFS는 재귀를 사용하지 않는 방법이다.

'''

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리 
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차언 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

