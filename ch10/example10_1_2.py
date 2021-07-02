"""
10.1 예제 : 출전 순서 정하기(ID : MATCHORDER)
- 탐욕법
- 난이도 : 하
- 동적 계획법으로 해결하기에는 너무 시간이 오래 걸리는 문제
"""

import bisect # c++ multiset의 lower_bound를 대체하기 위해 사용

def order(russian, korean):
    n = len(russian)
    wins = 0

    ratings = sorted(korean)
    for rus in range(n):
        # 이길 수 없는 경우 : 한국 선수 중 레이팅이 가장 낮은 선수를 출전 시킴
        if ratings[len(ratings)-1] < russian[rus]:
            del ratings[0]
        # 이길 수 있는 경우 : 이길 수 있는 선수 중 레이팅이 가장 낮은 선수를 출전 시킴
        else:
            lower_bound_index = bisect.bisect_left(ratings, russian[rus])
            del ratings[lower_bound_index]
            wins += 1

    return wins

for tc in range(int(input())):
    n = int(input())
    russian = list(map(int, input().split()))
    korean = list(map(int, input().split()))

    print(order(russian, korean))