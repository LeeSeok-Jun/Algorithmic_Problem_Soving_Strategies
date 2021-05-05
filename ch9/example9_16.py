"""
9.16 예제 : 틱택토
- 조합 게임
- 난이도 : 하
"""

# 2021/05/05

# turn에 해당하는 사람이 한 줄을 완성했는지 검사
def isFinished(board, turn):
    # 가로줄 확인
    for r in range(3):
        for c in range(3):
            if board[r][c] != turn:
                break

            # c가 2가 될 때 까지 반복문을 중단하지 않았다면 해당 가로줄은 모두 turn과 같은 모양
            if c == 2:
                return True
            
    # 세로줄 확인
    for c in range(3):
        for r in range(3):
            if board[r][c] != turn:
                break

            # r이 2가 될 때 까지 반복문을 중단하지 않았다면 해당 세로줄은 모두 turn과 같은 모양
            if r == 2:
                return True

    # 우하향 대각선 확인
    for r in range(3):
        if board[r][r] != turn:
            break

        if r == 2:
            return True
    
    # 좌하향 대각선 확인
    for r in range(3):
        if board[r][2-r] != turn:
            break

        if r == 2:
            return True

    return False

# 3*3 크기의 board 상태를 9자리의 3진수 숫자 구성으로 표현하고
# 이를 십진수 숫자로 변환하는 함수
# ex) board : 010/020/100 -> 2358
def bijection(board):
    result = 0

    for r in range(3):
        for c in range(3):
            result *= 3
            
            if board[r][c] == 'o':
                result += 1
            elif board[r][c] == 'x':
                result += 2

    return result

# 내가 이길 수 있으면 1, 비길 수 있으면 0, 질 수 밖에 없으면 -1
def canWin(board, turn):
    # 기저 사례 : 마지막에 상대가 이기는 수를 둘 경우(패배)
    if isFinished(board, ('o'+'x').replace(turn, "")):
        return -1

    # 메모이제이션
    if cache[bijection(board)] != -2:
        return cache[bijection(board)]

    # 모든 반환 값의 min 값을 취함
    minValue = 2
    for r in range(3):
        for c in range(3):
            if board[r][c] == '.':
                # python에서 문자열의 일부를 직접 변환하는 것은 불가능하기 때문에 문자열 자체를 바꿔야 한다.
                temp = list(board[r]) # 원 문자열을 리스트로 변환하고
                temp[c] = turn # 바꾸고자 하는 부분의 원소를 변경하고
                board[r] = ''.join(temp) # 다시 문자열로 만들어 기존 문자열을 대체

                minValue = min(minValue, canWin(board, ('o'+'x').replace(turn, ""))) # 상대방의 수에 대한 재귀 호출 진행
                
                # 원래 게임 보드판 형태로 복원
                temp[c] = '.'
                board[r] = ''.join(temp)

    if minValue == 2 or minValue == 0:
        cache[bijection(board)] = 0
        return cache[bijection(board)]

    # minValue(상대방의 수)가 -1이면 cache는 1이 저장되어 이길 수 있다는 의미가 되고
    # minValue가 1이면 cache에는 -1이므로 진다는 의미가 된다.
    cache[bijection(board)] = -minValue
    return cache[bijection(board)]

for tc in range(int(input())):
    board = []
    x_num = 0
    o_num = 0
    for r in range(3):
        board.append(input())
        # 현재 게임판에 존재하는 x와 o의 개수를 저장
        for c in range(3):
            if board[r][c] == 'x':
                x_num += 1
            elif board[r][c] == 'o':
                o_num += 1

    # 틱택토는 항상 x가 선플레이어이므로 x가 더 많으면 o 차례, 같은 경우는 x 차례
    if x_num > o_num:
        turn = 'o'
    else:
        turn = 'x'
    
    # cache 초기화
    # 19683 = 3^9
    # 게임판이 모두 x여서 3진수 222/222/222로 표현될 때 이를 10진수로 변환하면 19682이 된다.
    cache = [-2] * 19683

    answer = canWin(board, turn)
    # 비기는 경우
    if answer == 2 or answer == 0:
        print("TIE")
    # 이기는 경우
    elif answer == 1:
        print(turn)
    # 지는 경우
    else:
        print(('o'+'x').replace(turn, ""))