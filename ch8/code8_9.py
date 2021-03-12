"""
8.4 예제 : 삼각형 위의 최대 경로
- 전통적 최적화 문제들
- 난이도 : 하
- 문제 유형 : 동적 계획법
"""

n = int(input())

triangle = []
cache = [[-1] * n for _ in range(n)]
for i in range(n):
    triangle.append(list(map(int, input().split())))

def path(r, c):
    if r == n-1:
        return triangle[r][c]

    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = max(path(r + 1, c), path(r + 1, c + 1)) + triangle[r][c]
    return cache[r][c]

print(path(0, 0))
