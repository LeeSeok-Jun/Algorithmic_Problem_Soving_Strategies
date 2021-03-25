"""
8.14 문제 : 폴리오미노
- 난이도 : 중
- 시간 복잡도 : O(n^3)
    * 연결될 수 있는 경우의 수 * 만들 수 있는 폴리오미노의 수 * poly() 계산하는데 걸리는 시간
"""

# 2021/03/25

MOD = int(10e7)

# n개의 정사각형에 대해서 첫 줄이 first개인 폴리오미노의 수를 반환
def poly(n, first):
    # 기저 사례 : 한 줄을 모든 사각형으로 구섣
    if n == first:
        return 1

    # 메모이제이션
    if cache[n][first] != -1:
        return cache[n][first]

    cache[n][first] = 0

    # second는 최대 n-first까지 증가할 수 있음을 유의!
    # range(1, n-first)는 틀림...
    for second in range(1, n-first+1):
        add = first + second - 1 # 첫 번째 줄과 연결될 수 있는 하위 폴리오미노의 경우의 수
        add *= poly(n-first, second) # 경우의 수 * 만들 수 있는 폴리오미노 모양의 수
        add %= MOD

        cache[n][first] += add
        cache[n][first] %= MOD

    return cache[n][first]

for tc in range(int(input())):
    n = int(input())
    cache = [[-1] * (n+1) for _ in range(n+1)]

    answer = 0
    # 첫 번째 줄의 사각형이 1개 있는 경우부터 해서 n개 있는 경우까지 합
    for first in range(1, n+1):
        answer += poly(n, first)

    print(answer % MOD)