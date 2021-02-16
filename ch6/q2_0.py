"""
6.5 문제 : 게임판 덮기
- 난이도 : 하
"""

# 2021/02/16 13:55 ~ 14:59
# 가능한 블럭의 모양을 배열을 통해 구현

"""
def checkComplete(temp):
    for i in range(h):
        for j in range(w):
            if temp[i][j] == '.':
                return False

    return True

def turnBlock(center, wing1, wing2):
    pass

def putBlock(temp, r, c):
    center = (r, c)
    wing1 = (r-1, c)
    wing2 = (r, c+1)
"""

# 블록의 모양을 상대적인 인덱스로 표현
block_type = [[(0, 0), (1, 0), (0, 1)],
              [(0, 0), (0, 1), (1, 1)],
              [(0, 0), (1, 0), (1, 1)],
              [(0, 0), (1, 0), (1, -1)]]

# t : 블럭 모양
# delta : 현재 게임판에 블럭 설치 여부 결정(1 : 설치 / -1 : 제거)
def setBlock(board, r, c, t, delta):
    possible = True
    
    for i in range(3):
        nr = r + block_type[t][i][0]
        nc = c + block_type[t][i][1]

        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            possible = False

        else:
            board[nr][nc] += delta
            
            # 값이 1이 넘어갈 경우 블록이 중복되어 설치되어있다고 간주
            if board[nr][nc] > 1:
                possible = False

    return possible

def cover(board):
    h = len(board)
    w = len(board[0])

    # 아직 채워지지 않은 가장 위쪽 왼쪽에 있는 칸을 찾음
    r, c = -1, -1

    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                r = i
                c = j
                break

        if r != -1:
            break

    # 기저 사례 : 모든 칸을 채웠으면 1을 반환
    if r == -1:
        return 1

    result = 0

    for t in range(4):
        # 게임판을 덮을 수 있는 경우, 재귀 호출을 통해 반복
        if setBlock(board, r, c, t, 1):
            result += cover(board)

        # 설치한 블럭 제거
        setBlock(board, r, c, t, -1)

    return result


for tc in range(int(input())):
    h, w = map(int, input().split())
    
    board = []
    for i in range(h):
        board.append(list(map(int, input().split())))

    """
    temp = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            temp[i][j] = board[i][j]
    """

    print(cover(board))

    

