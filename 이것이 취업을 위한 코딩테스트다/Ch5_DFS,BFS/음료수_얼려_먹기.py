"""
문제 : 음료수 얼려먹기
알고리즘 : DFS
"""

# 구멍 O : 0
# 칸막이 : 1

# 해결 방법
"""
1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서
값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.

2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하면,
연결된 모든 지점을 방문할 수 있다.

3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
"""
# N,M을 공백으로 구분하여 입력 받기
N,M = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))



# DFS로 특정한 노드를 방문한 뒤 연결된 모든 노드들도 방문
def dfs(x,y):

    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= N or y <= -1  or y >= M:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        # 해당 노드를 방문 처리
        graph[x][y]=1
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
print(result)
