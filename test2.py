# 어캐 풀었도랑..
# 제외를 하는 노드에 붙어있는 모든 것들을 -2로 지정하여
# 리프에 카운팅 안되게 만듦!!!

import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
d = int(input())
print(graph)

def dfs(v):
    graph[v] = -2 # -2로 접근 불가능하게 만듦
    print(v, end=' ')
    for i in range(len(graph)):
        if v == graph[i]:
            dfs(i)

dfs(d)
cnt = 0
for i in range(len(graph)):
    if graph[i] != -2 and i not in graph: # 그래프 리스트 안에 없으면(부모가 없으면) 리프노드 
        cnt += 1

print(graph)
print(cnt)
