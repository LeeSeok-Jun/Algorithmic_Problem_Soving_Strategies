"""
8.11 예제 : 우물을 기어오르는 달팽이
- m일 동안 n미터 이상 오를 확률 계산
- 비올 확률은 50%
- 비가 오면 하루에 2미터 날이 맑으면 1미터씩 우물을 기어 올라감
"""

# 완전 탐색 알고리즘으로 시작
# 각 조합을 m 조각으로 잘라 재귀 호출의 각 단계에서 하루 날씨가 맑을지, 비가 올지 결정
# climb(c) = 배열 c에 대해서 지금까지 만든 날씨 조합 c를 완성해 원소의 합이 n이상이 되도록 하는 방법의 수

# 점화식
# climb(c) = climb(c + [1]) + climb(c + [2])
# [x] : 배열 c 뒤에 x를 덧붙인 결과

# 그러나 배열 c의 종류가 너무 많기 때문에 메모이제이션 적용 불가능

# 부분 문제 정의 바꾸기
# climb(days, climbed) = 지금까지 만든 날씨 조합 c의 크기가 days 이상이고 그 원소들의 합이 climbed일 때, c를 완성해서 원소의 합이 n 이상이 되도록 하는 방법의 수
# 달팽이가 days일 동안 cimbed 미터를 기어올라 왔을 때, m일 전까지 n 미터 이상 기어오를 수 있는 경우의 수를 계산

# m일 동안 n미터 이상 오를 확률 계산
n, m = map(int, input().split())

cache = [[-1] * (2 * n + 1) for _ in range(n)]

# 경우의 수를 반환 -> 최종적으로 2^m으로 값을 나누어야 확률을 계산 가능
def climb(days, climbed):
    # 기저 사례 : m일이 모두 지난 경우
    if days == m:
        return 1 if climbed >= n else 0

    # 메모이제이션
    if cache[days][climbed] != -1:
        return cache[days][climbed]

    # 1미터 올라간 경우 + 2미터 올라간 경우
    cache[days][climbed] = climbed(days + 1, climbed + 1) + climbed(days + 1, climbed + 2)
    return cache[days][climbed]

# 만일 비올 확률이 75%면??
# 이 함수는 경우의 수가 아닌 확률을 직접 반환하게 된다.
def climb2(days, climbed):
    # 기저 사례 : m일이 모두 지난 경우
    if days == m:
        return 1 if climbed >= n else 0

    # 메모이제이션
    if cache[days][climbed] != -1:
        return cache[days][climbed]

    # 1미터 올라간 경우 + 2미터 올라간 경우
    cache[days][climbed] = 0.25 * climbed(days + 1, climbed + 1) + 0.75 * climbed(days + 1, climbed + 2)
    return cache[days][climbed]