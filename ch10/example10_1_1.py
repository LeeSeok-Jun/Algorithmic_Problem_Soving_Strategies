"""
10.1 예제 : 회의실 예약
- 탐욕법
"""


# 각 회의는 [begin, end) 구간 동안 회의실을 사용한다.
n = 11
begin = [2, 2, 0, 5, 3, 8, 2, 6, 0, 8, 9]
end = [4, 7, 4, 9, 5, 10, 4, 9, 7, 9, 10]

def schedule():
    order = []
    for i in range(n):
        order.append((begin[i], end[i]))

    order.sort()

    earliest = 0 # 다음 회의 중 시작이 가장 빠른 회의의 시작 시간
    selected = 0 # 지금까지 선택된 회의의 수

    for i in range(len(order)):
        meetingBegin = order[i][0]
        meetingEnd = order[i][1]

        if earliest <= meetingBegin:
            earliest = meetingEnd
            selected += 1

    return selected

print(schedule())