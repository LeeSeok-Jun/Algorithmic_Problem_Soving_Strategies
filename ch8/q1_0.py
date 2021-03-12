"""
8.2 문제 : 와일드카드
- 난이도 : 중
- 문제 유형 : 동적 계획법
"""

# 2021/03/08

# ? : 어떤 글자와도 대응
# * : 어떤 문자열에도 대응 -> 문제 해결의 걸림돌이 되는 부분
#     패턴 *가 나타날 때마다 쪼개면 이 패턴이 문자열에 대응되는지 확인하는 문제를 m+1 조각으로 분해 가능
#     ex. t*l?*o*r?ng*s -> [t*, l?*, o*, r?ng*, s] (4개의 * 패턴이 존재해 문자열을 5개로 분해)

# 완전 탐색 알고리즘을 통한 구현
# 시간이 너무 오래 걸릴 수 있다.
# ******a 와 aaaaaab의 경우 결과적으로 불일치하지만 완전 탐색은 어째꺼나 모두 검사한다.
# w와 s는 문자열
def match(w, s):
    pos = 0

    # while이 끝나는 경우
    # 1. w[pos] != s[pos] : 무조건 대응 실패
    # 2. pos가 w의 끝에 도달 : 패턴에 *가 없는 경우
    # 3. pos가 s의 끝에 도달 : w에는 패턴이 남았지만 s는 끝남
    #                         w의 남은 패턴이 모두 *일때만 참, 나머지는 거짓 -> 4의 사례에서 재귀호출로 해결
    # 4. w[pos] == * : match(w', s')로 재귀호출 하여 하나라도 참이면 답은 참
    #                  w' : w의 pos+1 부터의 문자열
    #                  s' : s + skip 이후의 문자열 (skip은 0부터 증가하는 인덱스 변수)
    while(pos < len(w) and pos < len(s) and (w[pos] == "?" or w[pos] == s[pos])):
        pos += 1

    # 왜 while문이 종료되었는지 검사
    # 2의 사례 : w의 끝에서 종료하면 s역시 종료했는지 검사
    if pos == len(w):
        return pos == len(s) # True를 반환하면 대응 가능, False면 대응 불가능

    # 4의 사례 : *에 몇 글자를 대응해야 할지 재귀 호출로 확인
    if w[pos] == '*':
        skip = 0
        while (pos + skip <= len(s)):
            if match(w[pos+1:], s[pos+skip:]):
                return True # 하나라도 참이면 두 문자열은 대응
            skip += 1

    return False # 이 외의 경우는 모두 대응되지 않는 것으로 간주


# 메모이제이션을 통한 동적 계획법 알고리즘(cache 사용)
# w와 s의 인덱스를 가리키기 위한 매개변수 wi, si를 사용
# 패턴과 문자열의 길이가 모두 n인 경우 부분문제의 개수는 n^2
# 한 번 호출시 최대 n번의 재귀 호출
# 시간 복잡도 : O(n^3)
def matchMemoized(w, s, wi, si, cache):
    # 기존의 계산된 결과인 경우 그 결과값을 반환
    if cache[wi][si] != -1:
        return cache[wi][si]

    while(si < len(s) and wi < len(w) and (w[wi] == "?" or w[wi] == s[si])):
        wi += 1
        si += 1

    # while문이 왜 종료되었는지 검사
    if wi == len(w):
        if si == len(s):
            cache[wi][si] = 1
        else:
            cache[wi][si] = 0

        return cache[wi][si]

    if w[wi] == '*':
        skip = 0
        while (si + skip <= len(s)):
            if matchMemoized(w, s, wi+1, si+skip, cache):
                return 1

    return 0

# 시간 복잡도를 O(n^2)로 좀 더 단순하게 만드는 방법
# 반복문을 없애면 O(n^3) 에서 O(n^2)으로 바꿀 수 있다.
def matchMemoized2(w, s, wi, si, cache):
    if cache[wi][si] != -1:
        return cache[wi][si]

    # while 반복문으로 없애고 if를 통해 재귀 호출
    if (wi < len(w) and si < len(s) and (w[wi] == "?" or w[wi] == s[si])):
        cache[wi][si] = matchMemoized2(w, s, wi + 1, si + 1, cache)
        return cache[wi][si]

    if wi == len(w):
        if si == len(s):
            cache[wi][si] = 1
        else:
            cache[wi][si] = 0

        return cache[wi][si]
    
    if w[wi] == '*':
        if matchMemoized2(w, s, wi+1, si, cache) or (si < len(s) and matchMemoized2(w, s, wi, si+1, cache)):
            return 1

    return 0

for tc in range(int(input())):
    w = input() # 와일드카드

    n = int(input())
    matched = []

    for _ in range(n):
        s = input() # 파일명

        # -1 : 아직 답이 계산되지 않음
        # 1 : 해당 입력이 서로 대응됨(True)
        # 0 : 해당 입력이 서로 대응되지 않음(False)
        cache = [[-1] * (len(s) + 1) for _ in range(len(w) + 1)] # 문자열의 길이는 최대 100으로 조각으로 나누면 최대 101개로 나뉜다. (101 * 101)
        if matchMemoized2(w, s, 0, 0, cache) == 1:
            matched.append(s)

    matched.sort()
    for i in range(len(matched)):
        print(matched[i])
        
