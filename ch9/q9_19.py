"""
9.19 문제 : 블록 게임
- 난이도 : 중
- 조합 게임
- 동적 계획법
"""

# 2021/05/10

# 비트마스크를 사용해 게임판에 블록이 있는지 확인
# (r, c)에 위치한 블록은 r * 5 + c 번째 비트의 상태로 검사
cell = lambda r, c : 1<<(r * 5 + c)

# 게임판에 놓을 수 있는 블록들의 위치를 미리 계산한다.
def precalc():
    # 3칸 짜리 L자 모양의 블록의 위치를 미리 계산
    for r in range(4):
        for c in range(4):
            cells = []
            for dr in range(2):
                for dc in range(2):
                    cells.append(cell(r + dr, c + dc))

            square = cells[0] + cells[1] + cells[2] + cells[3]

            for i in range(4):
                moves.append(square - cells[i])

    # 2칸 짜리 블록의 위치를 미리 계산
    for i in range(5):
        for j in range(4):
            moves.append(cell(i, j) + cell(i, j+1))
            moves.append(cell(j, i) + cell(j+1, i))


# 현재 게임판 상태가 board일 때, 현재 차례인 사람이 승리할지 여부를 반환한다.
def play(board):
    # 메모이제이션
    if cache[board] != -1:
        return cache[board]

    cache[board] = 0
    
    # 모든 수를 고려한다.
    for i in range(len(moves)):
        # 현재 수를 게임판에 놓을 수 있는지 확인
        if (moves[i] & board) == 0:
            if not play(board | moves[i]):
                cache[board] = 1
                break

    return cache[board]

for tc in range(int(input())):
    game_board = []
    bit_board = 0
    for i in range(5):
        game_board.append(input())
        for j in range(5):
            if game_board[i][j] == "#":
                bit_board = bit_board | cell(i, j)

    moves = []

    cache = [-1] * int(1<<25)

    precalc()

    if play(bit_board) == 1:
        print("WINNING")
    else:
        print("LOSING")
