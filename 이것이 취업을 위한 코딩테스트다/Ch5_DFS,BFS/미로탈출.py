"""
문제 : 미로 탈출
"""

from collections import deque
# N,M 입력
N,M = map(int,input().split())

# 그래프 생성
graph = []
for i in range(N):
    graph.append(list(map(int,input())))



# 움직일 수 있는 방향(상,하,좌,우)
dx =[-1,1,0,0]
dy =[0,0,-1,1]


def BFS(x,y):

    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어나는 경우 다시 위로
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문한 경우에만 최단 거리 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]


print(BFS(0,0))