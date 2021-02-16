"""
6.2 예제 : 보글 게임
- 난이도 : 하
- 시간 복잡도 분석
    * 단어의 길이가 N 일때, 탐색은 N-1번 진행
    * 각 칸에는 최대 8개의 인접한 알파벳이 존재
    * 따라서 검사하는 후보의 수는 최대 8^N-1 번
    * 시간 복잡도는 O(8^N)
"""

# 2021/02/10 14:52 ~ 15:30

board = [['U', 'R', 'L', 'P', 'M'], ['X', 'P', 'R', 'E', 'T'], ['G', 'I', 'A', 'E', 'T'], ['X', 'T', 'N', 'Z', 'Y'], ['X', 'O', 'Q', 'R', 'S']]
visited = [[0] * 5 for _ in range(5)]

# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

# 내가 생각한 방법 - 실패
# 기저 사례를 올바르게 정의하지 못함
# 재귀 호출의 각 단계에서 반환하는 방법을 잘 못 지정함
"""
def hasWord(r, c, word):
    if len(word) == 1:
        return True

    if board[r][c] == word[0]:
        visited[r][c] = 1

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
                if board[nr][nc] == word[1] and visited[nr][nc] == 0:
                    return hasWord(nr, nc, word[1:])

    else:
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
                return hasWord(nr, nc, word)

    return False

print(hasWord(0, 0, 'PRETTY'))
"""

# 구현 답안
def hasWord(r, c, word):
    # 기저 사례 1: 시작 위치가 범위 밖이면 실패
    if r < 0 or r >= 5 or c < 0 or c >= 5:
        return False

    # 기저 사례 2 : 첫 글자가 일치하지 않으면 실패
    if board[r][c] != word[0]:
        return False

    # 기저 사례 3 : 남은 단어의 수가 1이면 성공
    if len(word) == 1:
        return True

    # 인접한 8칸 검사
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
            if hasWord(nr, nc, word[1:]):
                return True

    return False

print(hasWord(0, 0, 'PRETTY')) # False
print(hasWord(1, 1, 'PRETTY')) # True

