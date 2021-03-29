"""
8.16 문제 : 두니발 박사의 탈옥
- 난이도 : 중
- 문제 유형 : 동적 계획법
"""

# 2021/03/26

# 완전 탐색으로 구현
# search(path) : path로 시작하는 모든 경로를 다 만들고 이 중 q에서 끝나는 것들의 출현 확률의 합을 계산
def search(path):
    # 기저 사례 : d일이 경과
    # path의 크기가 d+1이면 인덱스 d를 검사 -> d번째 날 박사의 위치
    if len(path) == d+1:
        # 경로가 q에서 끝나지 않는다면 무효
        if path[-1] != q:
            return 0.0

        # 경로가 q에서 끝날 때 해당 경로가 나올 단일 확률 계산
        result = 1.0
        for i in range(len(path)-1):
            result /= degree[path[i]]

        return result

    # 만들 수 있는 모든 경로들을 생성
    for next in range(n):
        if connected[path[-1]][next] == 1:
            path.append(next)

            result += search(path) # 위 기저 사례에서 경로가 q에서 끝나는 단일 확률들의 합을 통해 전체 확률을 계산
            
            path.pop()

    return result

# 메모이제이션으로 구현
# search2(here, days) : days일째 here번 마을에 숨어 있을 때, 마지막 날 q번 마을에 있을 조건부 확률
# nd의 부분 문제를 갖고 각각 n 시간에 해결하므로 전체 시간 복잡도는 O(n^2d)
# 그러나 테스트 케이스 t개가 존재 하므로 총 O(n^dt)
def search2(here, days):
    # 기저 사례 : d일이 경과
    if days == d:
        # d일째(마지막 날) q번 마을에서 d일째(마지막 날) q번 마을에 있을 확률은 1
        # d일째(마지막 날) 다른 마을에서 d일째(마지막 날) q번 마을에 있을 확률은 0
        return 1.0 if here == q else 0.0

    # 메모이제이션
    # cache[here][days] : days일 째 here번 마을에서 계속 이동을 진행할 때 d일째(마지막 날) q번 마을에 도착할 확률을 저장
    if cache[here][days] > -0.5:
        return cache[here][days]

    cache[here][days] = 0.0
    for next in range(n):
        if connected[here][next]:
            # degree[here]로 나누눈 이유? 다음 날 next로 갈 확률을 의미
            cache[here][days] += search2(next, days+1) / degree[here]

    return cache[here][days]

# 테스트 케이스 t에 구애받지 않는 O(n^2d) 알고리즘
# q부터 해서 역으로 계산하는 방법
# search3(here, days) : 탈옥 후 days일째에 박사가 here번 마을에 숨어있을 확률
def search3(here, days):
    # 기저 사례 : 0일째
    # 0번째 날 p번 마을에서 0번째 날 p번 마을에 있을 확률은 1
    # 0번째 날 다른 마을에서 0번째 날 p번 마을에 있을 확률은 0
    if days == 0:
        return 1.0 if here == p else 0.0

    # 메모이제이션
    # cache[here][days] : days일 째 here번 마을에 박사가 숨어있을 확률을 저장
    if cache[here][days] > -0.5:
        return cache[here][days]

    cache[here][days] = 0.0
    for prev in range(n):
        if connected[prev][here]:
            # degree[prev]로 나누눈 이유? 전날 prev에서 here로 올 확률을 의미
            cache[here][days] += search3(prev, days-1) / degree[prev]

    return cache[here][days]

for tc in range(int(input())):
    n, d, p = map(int, input().split())

    connected = [] # 전체 마을 연결 정보를 저장
    degree = [0] * n # i번 마을에 대해 인접해 있는 마을의 수 저장
    for i in range(n):
        connected.append(list(map(int, input().split())))
        for j in range(n):
            if connected[i][j] == 1:
                degree[i] += 1

    t = int(input())
    qs = list(map(int, input().split()))

    # search2()
    # for q in qs:
    #     cache = [[-1] * d for _ in range(n)] # q가 바뀔때 마다 새롭게 cache를 갱신해야 함

    #     if q == qs[-1]:
    #         print(search2(p, 0))
    #     else:
    #         print(search2(p, 0), end=" ")

    # search3()
    cache = [[-1] * (d+1) for _ in range(n)] # q에 대해서 새롭게 cache를 갱신할 필요 없음!

    for q in qs:
        if q == qs[-1]:
            print(search3(q, d))
        else:
            print(search3(q, d), end=" ")