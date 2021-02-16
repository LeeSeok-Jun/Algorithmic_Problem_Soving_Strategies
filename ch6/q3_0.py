"""
6.8 문제 : 시계 맞추기
- 난이도 : 중
""" 

# 2021/02/16 15:34 ~ 16:12
# 내가 생각했던 방법이 큰 그림에서는 비슷함.
# 하나의 스위치는 최대 3번까지 누를 수 있고 4번 누르면 처음 상태로 돌아가는 것을 생각해야함.

INF = int(1e9)

switch = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

def check(data):
    isEnd = True

    for i in range(16):
        if data[i] != 12:
            isEnd = False

    return isEnd

def push(data, num_switch):
    for i in switch[num_switch]:
        data[i] += 3
        if data[i] > 12:
            data[i] -= 12

# 0번 스위치 부터 9번 스위치까지 눌러보면서 하나의 스위치가 몇 번씩 눌렸는지 누적함
def click(data, num_switch):
# def click(data, num_click)
    # if check(data):
    #     return num_click

    if num_switch == 10:
        if check(data):
            return 0
        else:
            return INF

    result = INF

    # for i in range(10):
    #     for j in switch[i]:
    #         data[j] += 3
    #         if data[j] > 12:
    #             data[j] -= 12

    #     candid = click(data, num_click + 1)
    #     result = min(result, candid)

    #     for j in switch[i]:
    #         data[j] -= 3
    #         if data[j] <= 0:
    #             data[j] += 12

    # 모든 스위치는 4번 누르면 처음 상태로 돌아간다.
    # i가 스위치를 누른 횟수를 저장함(어떤 스위치든 최대 3번까지 누를 수 밖에 없다.)
    for i in range(4):
        result = min(result, i + click(data, num_switch + 1))
        push(data, num_switch)

    return result


for tc in range(int(input())):
    data = list(map(int, input().split()))

    print(click(data, 0))