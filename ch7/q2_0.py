"""
7.4 문제 : 울타리 잘라내기
- 난이도 : 중
"""

# left, right 사이에서 가장 범위가 넓은 사각형을 찾는다.
def solve(left, right):
    # 기저 사례 1: 판자가 하나밖에 없는 경우
    if left == right:
        return data[left]

    # left ~ mid, mid+1 ~ right의 두 구간으로 문제를 분할
    # 부분 분제 1 : 가장 범위가 넓은 사각형이 좌측에 있는 경우
    # 부분 문제 2 : 가장 범위가 넓은 사각형이 우측에 있는 경우
    mid = (left + right) // 2

    # 분할한 문제들을 다시 재귀적으로 호출하고 가장 큰 값을 취함
    result = max(solve(left, mid), solve(mid+1, right))

    # 부분 문제 3 : 가장 범위가 넓은 사각형이 중앙에 걸쳐 있는 경우
    # 먼저, 중앙의 두 판자만 고려하는 너비가 2인 사각형을 확인
    low = mid
    high = mid+1
    # height = min(low, high) : 실수한 부분
    height = min(data[low], data[high])

    # 2 * height = 중앙의 두 판자를 이용한 사각형의 넓이
    # 판자가 이 단계에서 2개 밖에 없으므로 2(가로) * height(세로) 입력
    result = max(result, 2 * height)

    # 중앙의 사각형을 좌, 우로 점차 확대해가면서 모든 판자들에 대해서 확인
    while (left < low or high < right):
        # 항상 높이가 높은쪽으로 확장

        # 1. 오른쪽으로 확장하는 경우
        # 사각형의 오른쪽 부분이 전체 판자 내부에 위치하고,
        # 사각형의 왼쪽 부분이 제일 왼쪽에 위치한 판자이거나 오른쪽 판자의 높이가 왼쪽 판자의 높이보다 큰 경우 오른쪽으로 확장
        if high < right and (low == left or data[low - 1] < data[high + 1]):
            high += 1
            height = min(height, data[high]) # 사각형의 최대 높이를 새로 계산

        # 2. 왼쪽으로 확장하는 경우
        else:
            low -= 1
            height = min(height, data[low]) # 사각형의 최대 높이를 새로 계산

        result = max(result, height * (high - low + 1)) # 확장 후 사각형의 넓이를 새로 계산

    return result


for tc in range(int(input())):

    n = int(input()) # 울타리를 구성하는 판자의 수
    data = list(map(int, input().split())) # 판자의 높이 정보를 저장하는 리스트

    print(solve(0, n-1))