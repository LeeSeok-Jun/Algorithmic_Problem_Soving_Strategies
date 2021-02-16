"""
6.7 예제 : 여행하는 외판원 문제
"""

# 2021/02/16 15:16 ~ 15:30

n = int(input())
INF = int(1e9)

dist = []
for i in range(n):
    dist.append(list(map(int, input().split())))

path = [0]
visited = [False] * n
visited[0] = True

def shortestPath(path, visited, current):
    # 기저 사례 : 모든 도시를 방문했을 경우, 시작 도시로 돌아가 종료함
    if len(path) == n:
        return current + dist[path[0]][path[len(path)-1]]

    result = INF

    for next in range(n):
        # 이미 방문했다면 다음 반복으로
        if visited[next]:
            continue

        here = path[len(path)-1]
        path.append(next)

        visited[next] = True
        
        candid = shortestPath(path, visited, current + dist[here][next])

        result = min(result, candid)
        visited[next] = False
        path.pop(len(path)-1)

    return result

print(shortestPath(path, visited, 0))