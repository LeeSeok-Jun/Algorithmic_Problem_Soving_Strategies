"""
9.12 문제 : 웨브바짐
- 난이도 : 상
- 동적 계획법 테크닉
- 문제 해결 실패....
"""

# 2021/04/16

MOD = int(1e9) + 7

# 완전 탐색 알고리즘
# e의 자릿수로 만들 수 있는 숫자를 모두 출력
# price : 지금까지 만든 가격
# taken : 각 자릿수의 사용 여부(= Boolean 리스트)
def generate(price, taken):
    # 기저 사례 : 모든 자릿수를 사용
    if len(price) == n:
        if int(price) < e:
            print(price)
        return

    for i in range(n):
        # 해당 숫자가 사용된 적이 없고(taken[i] == False -> not taken[i])
        # 첫 번째로 사용한 숫자(i == 0)거나 이전 숫자와 자릿수가 다르거나(digit[i-1] != digit[i]) 이전 숫자가 이미 사용된 경우(taken[i-1] == True)
        if (not taken[i]) and (i == 0 or digit[i-1] != digit[i] or taken[i-1]):
            taken[i] = True
            generate(price + digit[i], taken)
            taken[i] = False

# 메모이제이션 적용
# index : 이번에 채울 자리의 인덱스
# taken : 지금까지 사용한 자릿수의 집합
# mod : 지금까지 만든 가격의 m에 대한 나머지
# less : 지금까지 만든 가격과 e의 비교 (e보다 작으면 1, 크면 0)
def price(index, taken, mod, less):
    # 기저 사례 : 모든 자릿수를 사용
    if index == n:
        return 1 if less and mod == 0 else 0

    # 메모이제이션
    if cache[taken][mod][less] != -1:
        return cache[taken][mod][less]

    cache[taken][mod][less] = 0

    for next in range(n):
        if (taken and 1<<next) == 0:
            # 과거 가격은 항상 현재 가격보다 낮아야 한다.
            if (not less) and e[index] < digit[next]:
                continue
            
            # 같은 숫자는 한 번만 선택
            if (next > 0) and (digit[next-1] == digit[next]) and (taken & 1<<(next-1) == 0):
                continue

            nextTaken = taken | 1<<next
            # 이 부분 형 변환 필요
            nextMod = (mod * 10 + digit[next] - '0') % mod
            nextLess = less or e[index] > digit[next]

            cache[taken][mod][less] += price(index+1, nextTaken, nextMod, nextLess)
            cache[taken][mod][less] %= MOD

    return cache[taken][mod][less]

for tc in range(int(input())):
    e, m = map(int, input().split())
    digit = list(str(e)) # digit를 어떻게 생성해야 될지 모르겠다..
    n = len(digit)
    
    cache = [[[-1] * 2] * 20 for _ in range(1<<14)] # 3차원 배열의 선언이 이게 맞는지?

    print(price(0, 0, 0, 0))