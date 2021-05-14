"""
9.22 문제 : 회전초밥
- 난이도 : 중
- 동적 계획법 테크닉
"""

# 2021/05/14

# 재귀적 동적 계획법으로 구현하기
# sushi() : bidget 만큼의 예산을 초밥을 먹는 데 써서 얻을 수 있는 최대 선호도의 합
MAX_BUDGET = 100 # 실제로는 10억을 할당해야 함
cache = [-1] * (MAX_BUDGET + 1)

def sushi(budget):
    if cache[budget] != -1:
        return cache[budget]

    cache[budget] = 0

    for dish in range(n):
        if budget < price[dish]:
            continue

        cache[budget] = max(cahce[budget], sushi(budget-price[dish])+preference[dish])

    return cache[budget]

# 반복적 동적 계획법으로 구현하기
c = [0] * (MAX_BUDGET + 1)
def sushi2():
    result = 0

    for budget in range(1, m+1):
        c[budget] = 0
        for dish in range(n):
            if budget >= price[dish]:
                c[budget] = max(c[budget], c[budget - price[dish]] + preference[dish])

        result = max(result, c[budget])

    return result

# 초밥의 가격은 무조건 100의 배수라는 점을 이용한 반복적 동적 계획법
# 초밥의 최대 가격은 20,000원으로 100으로 나누어 약 200개의 저장공간을 할당(넉넉하게 201개로 설정)
def sushi3():
    result = 0
    c2[0] = 0

    for budget in range(1, m+1):
        candid = 0
        for dish in range(n):
            if budget >= price[dish]:
                candid = max(candid, c2[(budget - price[dish]) % 201] + preference[dish])

        c2[budget % 201] = candid
        result = max(result, candid)

    return result

for tc in range(int(input())):
    n, m = map(int, input().split())

    m = int(m / 100) # 예산을 100으로 나눔

    price = []
    preference = []
    for i in range(n):
        pri, pre = map(int, input().split())
        price.append(int(pri / 100)) # 초밥 가격을 100으로 나눔
        preference.append(pre)

    c2 = [0] * 201
    print(sushi3())