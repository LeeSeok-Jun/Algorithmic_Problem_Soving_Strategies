"""
9.17 문제 : 숫자 게임
- 난이도 : 하
- 조합 문제
- 미니맥스 알고리즘
"""

# 2021/05/06

EMPTY = -987654321

def play(left, right):
    # 기저 사례 : 게임판에 모든 수가 없어졌을 때
    if left > right:
        return 0

    if cache[left][right] != EMPTY:
        return cache[left][right]

    # 왼쪽이나 오른쪽의 수를 가져가는 경우
    cache[left][right] = max(board[left] - play(left+1, right), board[right] - play(left, right-1))

    # 왼쪽이나 오른쪽의 수를 2개 지우는 경우
    # 일단, 적어도 게임판에는 2개 이상의 수가 존재해야 한다.
    if right - left + 1 >= 2:
        cache[left][right] = max(cache[left][right], -play(left + 2, right)) # 좌측 숫자 2개 삭제
        cache[left][right] = max(cache[left][right], -play(left, right - 2)) # 우측 숫자 2개 삭제

    return cache[left][right]

for tc in range(int(input())):
    n = int(input())
    board = list(map(int, input().split()))

    cache = [[EMPTY] * n for _ in range(n)] # cache[left][right] : 현재 게임판의 가장 좌측값이 left, 우측값이 right일 때 최대 점수차

    print(play(0, n-1))