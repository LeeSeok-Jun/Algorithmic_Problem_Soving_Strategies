"""
9.4 문제 : 광학 문자 인식
- 난이도 : 상
- 마르코프 연쇄
"""

# 2021/04/07

# 입력의 크기가 크기 때문에 빠른 입력 방식을 위한 sys 패키지 호출 및 입력 방법 변환
import sys
input = sys.stdin.readline

# 확률을 그대로 사용하면 언더플로가 발생할 수 있으므로 로그값을 이용하기 위해 math 패키지 호출
import math

INF = int(1e200) # 무한대 설정

# Q[segment] 부터 채워서 얻을 수 있는 최대 g() 곱의 로그 값을 반환
# Q[segment - 1] == previousMatch라고 가정함
def recognize(segment, previousMatch):
    if segment == n:
        return 0
    
    if cache[segment][previousMatch] != 1:
        return cache[segment][previousMatch]
    
    cache[segment][previousMatch] = -INF # log10(0)은 음의 무한대

    # R[segment]에 대응되는 단어 찾기
    for thisMatch in range(m):
        # log로 변환된 확률이기 때문에 곱이 아닌 합 연산을 한다.
        # M[thisMatch][R[segment]]를 M[previousMatch][R[segment]]로 적는 실수함...
        candid = T[previousMatch][thisMatch] + M[thisMatch][R[segment]] + recognize(segment + 1, thisMatch)

        if cache[segment][previousMatch] < candid:
            cache[segment][previousMatch] = candid
            choice[segment][previousMatch] = thisMatch

    return cache[segment][previousMatch]

# 실제 원문 역산으로 구하기
def reconstruct(segment, previousMatch):
    choose = choice[segment][previousMatch]
    result = origin_words[choose]
    if segment < n-1:
        result = result + " " + reconstruct(segment + 1, choose)

    return result

# 문제 입-출력
# m : 원문에 출현할 수 있는 단어의 수
# q : 처리해야 할 문장의 수
m, q = map(int, input().split())

# 원문에 출현하는 단어 목록
origin_words = input().split()

# B[i] = i번 단어가 첫 단어로 출현할 확률
B = list(map(float, input().split()))

# T[i][j] = i번 단어의 다음 단어가 j번 단어일 확률(로그값으로 치환)
T = []
for i in range(m):
    T.append(input().split())
    for j in range(m):
        if float(T[i][j]) != 0.0:
            T[i][j] = math.log10(float(T[i][j])) # 로그값으로 치환
        else:
            T[i][j] = -INF

# M[i][j] = i번 단어를 j번 단어로 인식할 확률(로그 값으로 치환)
M = []
for i in range(m):
    M.append(input().split())
    for j in range(m):
        if float(M[i][j]) != 0.0:
            M[i][j] = math.log10(float(M[i][j])) # 로그값으로 치환
        else:
            M[i][j] = -INF

cache = [[1] * 502 for _ in range(102)]
choice = [[None] * 502 for _ in range(102)]

for _ in range(q):
    recognized = input().split()

    n = int(recognized[0])

    recognized_sentence = recognized[1:]
    # 분류기가 반환한 문장 중 단어들을 원문의 단어 번호로 대체하여 저장
    R = []
    for word in recognized_sentence:
        R.append(origin_words.index(word))

    recognize(0, 0)
    print(reconstruct(0, 0))