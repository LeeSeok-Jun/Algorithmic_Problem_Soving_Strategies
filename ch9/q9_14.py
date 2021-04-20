"""
9.14 문제 : 실험 데이터 복구하기
- 동적 계획법 테크닉
- 난이도 : 중
"""

# 2021/04/20

# 겹치는 부분 최대화 하기
# restore(last, used) : 마지막에 출현한 조각 last와 지금까지 출현한 조각의 집합 used가 주어질 때, 나머지 조각을 추가해서 얻을 수 있는 overlap()의 최대 합
def restore(last, used):
    # 기저 사례 : 모든 문자열 조각을 사용
    if used == (1<<k)-1:
        return 0

    # 메모이제이션
    if cache[last][used] != -1:
        return cache[last][used]

    cache[last][used] = 0

    for next in range(k):
        if (used & 1<<next) == 0:
            candid = overlap[last][next] + restore(next, used + (1<<next))

            cache[last][used] = max(cache[last][used], candid)

    return cache[last][used]

# 실제 문제에서 요구하는 문자열 출력
def reconstruct(last, used):
    # 기저 사례 : 모든 문자열 조각을 사용
    if used == (1<<k)-1:
        return ""

    # 다음에 올 문자열 조각을 찾음
    for next in range(k):
        # next가 이미 사용되었다면 제외
        if used & (1<<next):
            continue

        # next를 사용했을 경우 답이 최적해와 같다면 next 사용
        ifUsed = restore(next, used + (1<<next)) + overlap[last][next]
        if restore(last, used) == ifUsed:
            return words[next][overlap[last][next]:] + reconstruct(next, used + (1<<next)) # 이 부분이 이해하기가 어려움...

    return "!@#!@#ERROR!@#!@#"

# 두 문자열 a, b에 대해서 두 문자열이 얼마나 일치하는지를 반환
def overlapFunction(a, b):
    # a = "abcd", b = "cde"인 경우 i == 2 일때, a[2:] == b[:2] == "cd" 이므로 2를 반환한다.
    for i in range(min(len(a), len(b)), 0, -1):
        if a[len(a)-i:] == b[:i]:
            return i

    return 0

for tc in range(int(input())):
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input())
    
    overlap = [[0] * 15 for _ in range(15)] # 두 문자열이 얼마나 중복되는지 저장 -> overlapFunction()에서 사전에 계산 후 저장

    # cache[last][used] : 마지막 단어가 last고 사용하지 않은 단어가 used의 여잡합일 때, used의 여집합에 있는 단어들에 대한 중복도를 저장한다. -> restore() 에서 사용
    cache = [[-1] * int(1<<15) for _ in range(15)] # 후보가 되는 모든 문자열에 대해서 발생할 수 있는 최대 중복정도를 저장

    # 어떤 문자열이 다른 문자열의 완전한 부분 문자열인지 검사
    # 완전한 부분 문자열인 경우가 발생하면 무시해도 되기 때문에 이 과정이 필요함
    while True:
        check = False # True면 어떤 문자열이 다른 문자열의 완전한 부분 문자열임을 의미한다.

        for i in range(k):
            if not check:
                for j in range(k):
                    # 서로 다른 두 문자열에 대해서 어떤 문자열이 다른 문자열의 완전한 부분 문자열인 경우
                    if i != j and words[j] in words[i]:
                        words.pop(j) # 해당 문자열을 단어 목록에서 삭제
                        k -= 1 # 전체 단어의 수를 줄임
                        check = True

        # 만일 어떤 단어가 다른 단어의 완전한 부분 문자열인 경우 한 번더 검사를 진행
        # 완전히 검사가 끝났을 때 부분 문자열이 없을 경우에만 while 반복문 종료
        if not check:
            break

    # 두 단어만 고려했을 때의 중복정도를 이차원 리스트 overlap에 사전 저장 
    for i in range(k):
        for j in range(k):
            overlap[i][j] = overlapFunction(words[i], words[j])

    print(reconstruct(k, 0))