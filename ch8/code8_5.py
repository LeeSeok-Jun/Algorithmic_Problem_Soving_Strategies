"""
8.1 예제 : 외발 뛰기
"""

# 동적 계획법 알고리즘으로 구현
# jump(r, c) : (r, c)에서 맨 마지막 칸까지 도달할 수 있는지 여부를 반환
# 점화식 : jump(r, c) = jump(r + jumpSize, c) || jump(r, c + jumpSize)

n = int(input())
board = [[1] * n for _ in range(n)]

# 부분 문제의 결과값을 저장한다.
cache = [[-1] * n for _ in range(n)] # 메모이제이션을 위한 2차원 리스트

def jump2(r, c):
    if r >= n or c >= n:
        return 0 # False

    if r == n-1 and c == n-1:
        return 1 # True

    result = cache[r][c]

    # 기존에 부분 문제를 해결한 경우 그 결과값을 그대로 반환
    if result != -1:
        return result

    # 부분 문제를 해결한 적이 없다면 문제를 새롭게 해결
    jumpSize = board[r][c]

    # 메모이제이션 cache에 저장
    cache[r][c] = jump2(r + jumpSize, c) or jump2(r, c + jumpSize)

    return cache[r][c]

print(jump2(0, 0))