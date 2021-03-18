"""
8.9 문제 : 양자화
- 난이도 : 중
"""

# 2021/03/18

INF = int(10e9)

# array를 정렬하고 각 부분합을 계산
# pSum[] : array[]의 부분합을 저장 (pSum[i]는 array[0] ~ array[i]의 합)
# pSqSum[] : array[]의 제곱의 부분합을 저장 (pSqSum[i]는 array[0]^2 ~ array[i]^2의 합)
def precalc():
    array.sort()
    pSum[0] = array[0]
    pSqSum[0] = array[0] * array[0]

    for i in range(1, n):
        pSum[i] = pSum[i-1] + array[i]
        pSqSum[i] = pSqSum[i-1] + array[i] * array[i]

# array[low] ~ array[high] 구간을 하나의 숫자로 표현할 때 최소 오차 합을 계산
def minError(low, high):
    # 부분합을 이용하여 A[low]부터 A[high]까지의 합을 구함
    low_value = 0 if low == 0 else pSum[low-1]
    sum_value = pSum[high] - low_value

    sq_low_value = 0 if low == 0 else pSqSum[low-1]
    sq_sum_vlaue = pSqSum[high] - sq_low_value

    # 이 합의 평균을 반올림한 값으로 양자화 표현
    m = int(0.5 + sum_value / (high - low + 1))

    # sum(A[i]-m)^2을 전개한 결과를 부분 합으로 표현
    result = sq_sum_vlaue - 2 * m * sum_value + m * m * (high - low + 1)
    return result

def quantize(from_index, parts):
    # 기저 사례 1 : 모든 숫자를 양자화한 경우
    if from_index == n:
        return 0

    # 기저 사례 2 : 숫자는 아직 남아있는데 더 묶을 수 없어 아주 큰 값을 반환
    if parts == 0:
        return INF

    if cache[from_index][parts] != -1:
        return cache[from_index][parts]

    cache[from_index][parts] = INF
    
    # 조각의 길이를 변화시키며 최소치를 찾음
    partSize = 1
    while (from_index + partSize <= n):
        cache[from_index][parts] = min(cache[from_index][parts], minError(from_index, from_index + partSize - 1) + \
            quantize(from_index + partSize, parts - 1))
        partSize += 1

    return cache[from_index][parts]

for tc in range(int(input())):
    n, s = map(int, input().split())

    cache = [[-1] * 11 for _ in range(101)]
    pSum = [0] * 101
    pSqSum = [0] * 101

    array = list(map(int, input().split()))
    precalc()
    print(quantize(0, s))


