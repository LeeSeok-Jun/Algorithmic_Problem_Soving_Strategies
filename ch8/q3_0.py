"""
8.7 문제 : 원주율 외우기
- 난이도 : 하
- 입력되는 문자열의 길이는 8 ~ 10,000자리
- 첫 조각의 길이는 3, 4, 5 중의 하나이므로 각 경우마다 하나의 부분 문제를 풀어야 한다.
- 전체 문제의 최적해는 다음 세 경우 중 가장 작은 값
    * 길이 3인 조각의 난이도 + 3글자 빼고 나머지 수열에 대한 최적해
    * 길이 4인 조각의 난이도 + 4글자 빼고 나머지 수열에 대한 최적해
    * 길이 5인 조각의 난이도 + 5글자 빼고 나머지 수열에 대한 최적해
- n글자 빼고 나머지 수열에 대한 최적해에 대해서 재귀적으로 다시 위 세가지 부분 문제를 진행한다.
"""

# 2021/03/18

INF = int(10e9)

# begin : 수열의 시작 위치
# N[begin : begin + L] : N[begin]에서 시작하는 길이 L인 부분 문자열
# memorize() : 최소 난이도를 반환하는 함수
# classify() : 나뉜 조각의 난이도를 반환하는 함수 
# memorize(begin) = min(memorize(bigin + L) + classify(N[begin : begin+L])) (L은 3부터 5까지)

# N[a:b] 구간의 난이도를 반환
def classify(a, b):
    # 숫자 조각을 가져옴
    m = n[a:b+1]

    # 난이도가 1인 경우(모든 숫자가 같은 경우)
    if m == (m[0] * len(m)):
        return 1

    # 등차수열의 형태를 이루는지 검사
    progressive = True

    for i in range(len(m)-1):
        if (int(m[i+1]) - int(m[i])) != (int(m[1]) - int(m[0])):
            progressive = False

    # 난이도가 2인 경우(등차수열이며 모든 숫자가 등차가 1 or -1)
    if progressive and abs(int(m[1]) - int(m[0])) == 1:
        return 2

    # 난이도가 4인 경우(두 수가 번갈아 등장)
    alternating = True
    for i in range(len(m)):
        # (0, 0), (1, 1), (2, 0), (3, 1), (4, 0), (5, 1).....
        # 0,1의 인덱스에 해당하는 값과 홀수, 짝수의 인덱스에 해당하는 값이 같은지 검사하여 번갈아 나오는지 알 수 있음
        if m[i] != m[i%2]:
            alternating = False

    if alternating:
        return 4

    # 난이도가 5인 경우(등차가 1, -1이 아닌 등차수열의 형태)
    if progressive:
        return 5

    # 그 외의 경우는 모두 난이도가 10
    return 10

# N[begin:]을 외우는 방법 중 난이도의 최소 합을 반환
def memorize(begin):
    # 기저 사례 : begin이 문자열의 끝인 경우
    if begin == len(n):
        return 0

    if cache[begin] != -1:
        return cache[begin]

    cache[begin] = INF
    for L in range(3, 6):
        if begin + L <= len(n):
            cache[begin] = min(cache[begin], memorize(begin + L) + classify(begin, begin + L - 1))

    return cache[begin]
    
for tc in range(int(input())):
    n = input()
    cache = [-1] * 10002
    print(memorize(0))