"""
9.6 예제 : 모스 부호 사전
- 난이도 : 중
- k번째 답 계산하기
"""

# 2021/04/09
n, m, k = map(int, input().split())

# code9.6 모든 모스 신호를 만드는 완전 탐색 알고리즘
# n : 필요한 장점(-)의 수
# m : 필요한 단점(o)의 수
# s : 지금까지 만든 신호
def generate(n, m, s):
    # 기저 사례 : n = m = 0
    if n == 0 and m == 0:
        return
    
    if n > 0:
        generate(n-1, m, s + "-")
    
    if m > 0:
        generate(n, m-1, s + "o")

# code9.7 k-1개를 건너뛰고 첫 번째 신호를 출력하는 알고리즘
# skip개를 건너뛰고 출력한다.
# 일일이 코드를 만들기 때문에 k가 크면 시간 안에 답을 찾을 수 없다.
skip = k-1

def generate2(n, m, s):
    global skip
    # 기저 사례 1 : skip < 0
    # skip이 -1까지 감소했다는 의미는 이미 k번째 신호를 출력했다는 뜻이다.
    if skip < 0:
        return
    
    # 기저 사례 2 : n = m = 0
    if n == 0 and m == 0:
        # 더 이상 건너뛸 신호가 없는 경우 출력
        if skip == 0:
            print(s)

        skip -=1
        return

    if n > 0:
        generate2(n-1, m, s + "-")
    
    if m > 0:
        generate2(n, m-1, s + "o")

# code9.8 이항계수를 이용한 k-1개를 건너뛰고 k번째 신호를 출력하는 알고리즘
# n개의 장점과 m개의 단점을 s 뒤에 잇는 조합의 수는 이항계수 (n+m n)개

MAXIMUM = int(1e9)+100

# 계산에 필요한 모든 이항계수를 미리 계산한다.
bino = [[0] * (n + m + 1) for _ in range(n + m + 1)]

def calcBino():
    # bino = [[0] * (n + m + 1) for _ in range(n + m + 1)]
    for i in range(n + m + 1):
        bino[i][0] = bino[i][i] = 1
        
        for j in range(i):
            bino[i][j] = min(MAXIMUM, bino[i-1][j-1] + bino[i-1][j])

# skip개를 건너뛰고 출력
def generate3(n, m, s):
    global skip
    # 기저 사례 1 : skip < 0:
    if skip < 0:
        return
    
    # 기저 사례 2 : n = m = 0
    if n == 0 and m == 0:
        if skip == 0:
            print(s)
        
        skip -= 1
        return

    # 기저 사례 3 : skip이 (n+m m)보다 크거나 같으면 아직 답은 찾지 못하고 skip은 (n+m m)만큼 줄어있는 상태
    # 굳이 일일이 재귀 호출할 필요 없이 skip의 크기를 줄여버리고 종료해도 똑같은 결과가 나온다?
    if bino[n+m][n] <= skip:
        skip -= bino[n+m][n]
        return

    if n > 0:
        generate3(n-1, m, s + "-")
    
    if m > 0:
        generate3(n, m-1, s + "o")

# code9.9 n개의 -, m개의 o로 구성된 신호 중 skip개를 건너뛰고 만들어지는 신호를 반환
def kth(n, m, skip):
    # n == 0이면 나머지 부분은 o로 구성된 신호일 수 밖에 없다.
    if n == 0:
        return "o" * m

    if skip < bino[n+m-1][n-1]:
        return "-" + kth(n-1, m, skip)

    return "o" + kth(n, m-1, skip - bino[n+m-1][n-1])

calcBino()
generate3(n, m, "")
print(kth(n, m, k-1))
