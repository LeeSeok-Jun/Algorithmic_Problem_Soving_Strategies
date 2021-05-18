"""
9.24 문제 : 지니어스
- 난이도 : 중
- 반복적 동적 계획법
- 마르코프 연쇄(8.11, 9.1)
- 행렬의 거듭 제곱
"""

# 2021/05/18

import pprint


# start(time, song) = 재생을 시작한지 time분 후에 song번 노래가 재생을 시작할 확률
# 반복적 동적 계획법
def start1():
    # c[time][song] = time분 후에 song번 노래가 재생될 확률
    c = [[0] * 51 for _ in range(5)]
    c[0][0] = 1.0

    for time in range(1, k+1):
        for song in range(n):
            c[int(time % 5)][song] = 0
            for prev in range(n):
                c[int(time % 5)][song] += c[int((time - L[prev] + 5) % 5)][prev] * T[prev][song]

    result = [0] * n
    # song번 노래가 재생되고 있을 확률을 계산한다.
    for song in range(n):
        # song번 노래가 시작했을 때 시간을 모두 찾아 더함
        for starting in range(k-L[song]+1, k+1):
            result[song] += c[int(starting % 5)][song]

    return result 

# 행렬의 거듭 제곱을 이용한 풀이

# 행렬의 거듭 제곱 구하기
def mul(matrix1, matrix2):
    temp = [[0] * len(matrix1) for _ in range(len(matrix1))]

    for r in range(len(matrix1)):
        for c in range(len(matrix1)):
            for i in range(len(matrix1)):
                temp[r][c] += matrix1[r][i] * matrix2[i][c]

    return temp

def pow(k, matrix):
    if k == 1:
        return matrix
    elif k == 2:
        return mul(matrix, matrix)
    else:
        temp = pow(k//2, matrix)
        if k//2 == 0:
            return mul(temp, temp)
        else:
            return mul(mul(temp, temp), matrix)

def start2():
    W = [[0] * (4*n) for _ in range(4*n)]

    # 첫 3*n개의 원소는 그대로 복사
    for i in range(3*n):
        W[i][i+n] = 1.0

    # 마지막 n개의 원소는 이전 원소들의 선형 결합으로 이루어진다.
    for i in range(n):
        # c[time + 1][i] = c[time+1-L[j]][j] * T[j][i]
        for j in range(n):
            W[3*n+i][(4-L[j])*n + j] = T[j][i]

    Wk = pow(k, W)

    result = [0] * n
    for song in range(n):
        for starting in range(L[song]):
            result[song] += Wk[(3-starting)*n + song][3*n]

    return result

for tc in range(int(input())):
    # n : MP3 플레이어에 들어 있는 곡의 수
    # k : k분 30초 뒤에 재생될 노래에 대한 k의 값
    # m : 태윤이가 좋아하는 곡의 수
    n, k, m = map(int, input().split())

    L = list(map(int, input().split())) # n개의 노래에 대한 각 곡의 길이

    T = [] # 한 곡이 재생된 후 다음 곡이 재생될 확률을 나타내는 확률
    for _ in range(n):
        T.append(list(map(float, input().split())))

    Q = list(map(int, input().split())) # 태윤이가 좋아하는 m개의 곡의 번호

    answer = start2()

    for i in Q:
        print(answer[i], end=" ")

    print()