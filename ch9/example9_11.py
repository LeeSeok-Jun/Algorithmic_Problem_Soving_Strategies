"""
예제 9.11 : 여행하는 외판원 문제를 해결하는 동적 계획법 알고리즘
- 6.7 단원의 문제는 n!개의 경로를 모두 생성하는 완전 탐색 알고리즘으로 해결
- n = 15 이상인 경우에는 계산이 사실상 불가능
"""

# 2021/04/14

# 6.7 단원의 path는 다음과 같이 두 가지 용도로 사용한다.
# 1. 경로가 완성되었을 때 전체 경로의 길이를 계산 -> 남은 경로의 최소 길이와 현재 위치를 사용하자!
# 2. 어떤 도시를 방문한 적이 있는지 확인 -> 도시 방문 여부만 확인하자!

# 이를 응용하여 shortestPath2(here, visited)를 정의
# shortestPath2(here, visited) : 현재 위치가 here, 각 도시를 방문했는지 여부를 bool값으로 저장하는 리스트 visited가 주어질 때,
# here에서 시작해 나머지 도시를 방문하는 부분 경로의 최소 길이를 반환

n = int(input())
INF = int(1e9)

dist = []
for i in range(n):
    dist.append(list(map(int, input().split())))

# cache[here][visited] 형태로 저장
# visited는 마을의 통과 여부를 결정한다.
# bool 자료형을 메모이제이션하지 않고 비트 형태로 치환하여 사용
# 예를 들어 [True, False, True, False]인 경우 0b1010 같이 표현 가능
# 1<<4의 경우 0b10000 와 같이 1 뒤에 0이 4개 붙는 형식
cache = [[-1] * int(1<<n) for _ in range(n)]

def shortestPath2(here, visited):
    # 기저 사례 : 모든 도시를 모두 방문했으면 출발 도시로 돌아가고 종료한다.
    # 출발 도시는 항상 0번 도시라고 가정!
    # n == 4 일 때, (1<<4)-1을 하면 0b01111 이므로 모든 4개 도시에 대해 [True, True, True, True]와 같은 의미가 된다.(제일 큰 비트는 제외)
    # 이를 응용하여 모든 도시를 방문했는지 검사가 가능하다.
    if visited == (1<<n)-1:
        return dist[here][0] # 마지막 도시에서 출발지로 돌아가는 거리를 추가하기 위함

    # 메모이제이션
    if cache[here][visited] >= 0:
        return cache[here][visited]

    cache[here][visited] = INF

    # 다음 방문할 도시를 검사
    for next in range(n):
        # 이미 방문한 도시인 경우 건너뜀
        if visited & (1<<next):
            continue

        # 아직 방문하지 않은 도시들에 대해 최단 거리를 계산
        # 재귀적인 호출로 각 경로에 대해 모든 도시를 방문하는 거리를 계산한다.
        # visited + (1 << next)는 이 반복문을 통해 해당 도시를 방문했음을 의미한다.
        candid = dist[here][next] + shortestPath2(next, visited + (1<<next))

        # 모든 재귀 호출에 대해 최단 거리를 결정
        cache[here][visited] = min(cache[here][visited], candid)

    return cache[here][visited]

print(shortestPath2(0, 1<<(n-1)))