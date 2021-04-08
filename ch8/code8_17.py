"""
8.11 예제 : 삼각형 위의 최대 경로 개수 세기
- 난이도 : 중
"""

# count(r, c) = (r, c)에서 시작해 맨 아래줄까지 내려가는 최대 경로의 수
# 점화식
# count(r, c) = max(count(r+1, c), count(r+1, c+1), count(r+1,c) + count(r+1, c+1))

from code8_9 import path

countCache = [[-1] * 100 for _ in range(100)]

n = int(input())

# (r, c)에서 시작해서 맨 아래줄까지 내려가는 경로 중 최대 경로의 개수를 반환
def count(r, c) :
    # 기저 사례 : 맨 아래줄에 도달한 경우
    if r == n-1:
        return 1

    # 메모이제이션
    if countCache[r][c] != -1:
        return countCache[r][c]

    countCache[r][c] = 0

    if path(r+1, c+1) >= path(r+1, c):
        countCache[r][c] += count(r+1, c+1)
    
    if path(r+1, c+1) <= path(r+1, c):
        countCache[r][c] += count(r+1, c)

    return countCache[r][c]
