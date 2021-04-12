"""
9.7 문제 : k번째 최대 증가 부분 수열
- 난이도 : 상
- k번째 답 계산하기
"""

MAX = int(2e9)+1

# S[start]에서 시작하는 증가 부분 수열 중 최대 길이를 반환한다.
def lis(start):
    # 메모이제이션
    # start + 1을 사용하는 이유는 S[-1]이 있다고 가정하고 0번 인덱스부터 cache에 담기 위해(?)
    if cacheLen[start + 1] != -1:
        return cacheLen[start + 1]

    cacheLen[start + 1] = 1 # LIS에 항상 S[start + 1]는 있기 때문에 길이는 최하 1

    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            cacheLen[start + 1] = max(cacheLen[start + 1], lis(next) + 1)

    return cacheLen[start + 1]

# S[start]에서 시작하는 최대 증가 부분 수열의 수를 반환
def count(start):
    # 기저 사례 : LIS의 길이가 1인 경우
    if lis(start) == 1:
        return 1
    
    # 메모이제이션
    if cacheCnt[start + 1] != -1:
        return cacheCnt[start + 1]

    cacheCnt[start + 1] = 0
    for next in range(start+1, n):
        if (start == -1 or S[start] < S[next]) and (lis(start) == lis(next) + 1):
            cacheCnt[start + 1] = min(MAX, cacheCnt[start + 1] + count(next))

    return cacheCnt[start + 1]

# S[start]에서 시작하는 LIS 중 사전순으로 skip개 건너뛴 수열을 lis에 저장
def reconstruct(start, skip, lis_array):
    # S[start]는 항상 lis에 포함된다.
    if start != -1:
        lis_array.append(S[start])
    
    # 뒤에 올 수 있는 숫자들의 인덱스 목록을 만듦
    # (숫자, 숫자의 인덱스)형태로 저장
    followers = []
    # range(start + 1, n)을 그냥 (start + 1, n)로 적는 대참사 발생...
    for next in range(start + 1, n):
        if (start == -1 or S[start] < S[next]) and lis(start) == lis(next)+1:
            followers.append((S[next], next))
    
    followers.sort() # 숫자가 증가하는 순서대로 정렬

    # k번째 LIS의 다음 숫자를 찾는다.
    for i in range(len(followers)):
        # i번째 숫자를 S[start]뒤에 붙였을 때 만들 수 있는 LIS의 개수를 확인한다.
        idx = followers[i][1]
        cnt = count(idx)

        # 나올 수 있는 LIS의 수가 skip보다 적기 때문에 skip에서 해당 수 만큼 제외
        if cnt <= skip:
            skip -= cnt

        # 나올 수 있는 LIS의 수가 skip보다 많다면 k번(skip+1)째 LIS를 재귀 호출을 통해 구한다.
        # 또한, k번째 LIS에서 start 뒤에 올 원소는 idx임을 알 수 있다. 
        else:
            reconstruct(idx, skip, lis_array)
            break

# 문제 입-출력
for tc in range(int(input())):
    n, k = map(int, input().split())

    S = list(map(int, input().split()))

    cacheLen = [-1] * (n + 2) # i번째 인덱스에서 만들 수 있는 LIS의 최대 길이를 저장
    cacheCnt = [-1] * (n + 2) # i번째 인덱스에서 만들 수 있는 LIS의 최대 개수를 저장

    lis_array = []
    reconstruct(-1, k-1, lis_array)

    print(len(lis_array))
    print(lis_array)