"""
8.5 문제 : 합친 LIS(JLIS, 합친 증가하는 부분 수열)
- 난이도 : 하
- 문제 유형 : 동적 계획법
"""

# 2021/03/12
# 먼저 두 배열 a, b에 대해서 a[-1], b[-1](마지막 원소가 아님)에 -10e9가 이미 존재한다는 가정을 한다.
# 이 과정을 통해 배열을 0번 인덱스부터 순회하며 합친 증가하는 부분 수열을 찾을 수 있다.
# 만약 가정하지 않는다고 하면 a = [10, 20, 30, 1, 2] b = [10, 20, 30]인 경우 a의 원소 1, 2는 증가하는 부분수열에 고려하지 않는 문제가 발생
# -1 인덱스부터 순회하기 때문에 cache에 접근할 때는 인덱스에 +1을 할 필요가 있다. -> cache의 저장 크기도 1씩 증가함

def jlis(indexA, indexB):
    # 이미 계산된 결과가 있는 경우 해당 값 반환
    if cache[indexA + 1][indexB + 1] != -1:
        return cache[indexA + 1][indexB + 1]

    # indexA와 indexB의 최초 값은 -1부터 시작하기 때문에 cache에 접근할 때는 +1을 해줘야 정상적인 인덱스 접근이 가능하다.
    # cache[indexA + 1][indexB + 1] = 2 # JLIS 내부에는 적어도 A[indexA]와 B[indexB]가 들어있기 때문에 2를 초기 값으로 지정(?)
    cache[indexA + 1][indexB + 1] = 0
    
    # indexA와 indexB가 -1인 설정이 있어야 두 배열 내 가장 작은 원소를 기준으로 하는 증가하는 부분 수열을 탐색한다.
    tempA = -int(10e9) if indexA == -1 else a[indexA]
    tempB = -int(10e9) if indexB == -1 else b[indexB]
    maxElement = max(tempA, tempB) # 다음에 들어올 수 있는 원소에 대한 기준을 설정

    # 다음에 들어올 원소를 찾음
    # 기준값보다 큰 원소를 추가하여 증가하는 부분 수열을 재귀적으로 만들어 보고 기존의 값과 비교하여 나오는 최대 길이를 반환한다.
    # 원소가 추가되면 합친 LIS의 길이는 1씩 증가되는 것을 반영한다.
    for nextA in range(indexA + 1, n):
        if maxElement < a[nextA]:
            cache[indexA + 1][indexB + 1] = max(cache[indexA + 1][indexB + 1], jlis(nextA, indexB) + 1)
    
    for nextB in range(indexB + 1, m):
        if maxElement < b[nextB]:
            cache[indexA + 1][indexB + 1] = max(cache[indexA + 1][indexB + 1], jlis(indexA, nextB) + 1)

    return cache[indexA + 1][indexB + 1]

for tc in range(int(input())):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # cache를 통해 두 배열의 각 특정 인덱스에서 나올 수 있는 합친 LIS의 최대 길이를 저장
    # cache 배열의 마지막 부터(재귀 호출할 때 제일 깊숙히 들어가서 서서히 반환하기 때문?) 최적 부분 구조로 인한 최적화 결과가 누적되어 cache의 맨 처음에 저장
    cache = [[-1] * (m + 1) for _ in range(n + 1)]

    print(jlis(-1, -1))