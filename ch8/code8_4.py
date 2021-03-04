"""
8.1 예제 : 외발 뛰기
- 동적 계획법 알고리즘을 만드는 첫 단계는 해당 문제를 재귀적으로 해결하는 완전 탐색 알고리즘을 만든다.
"""

# 재귀 호출 알고리즘
# jump(r, c) : (r, c)에서 맨 마지막 칸까지 도달할 수 있는지 여부를 반환
# 점화식 : jump(r, c) = jump(r + jumpSize, c) || jump(r, c + jumpSize)

n = int(input())
board = [[1] * n for _ in range(n)]

def jump(r, c):
    # 기저 사례 1 : 보드판 바깥으로 넘어가는 경우
    if r >= n or c >= n:
        return False

    # 기저 사례 2 : 보드판 마지막 칸(목적지)에 도달하는 경우
    if r == n-1 and c == n-1:
        return True

    jumpSize = board[r][c]

    return jump(r + jumpSize, c) or jump(r, c + jumpSize)