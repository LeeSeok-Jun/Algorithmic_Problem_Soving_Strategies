"""
9.1 예제 : 최대 증가 부분 수열 실제로 출력하기
- 수열 S = [4, 7, 6, 9, 8, 10]의 최대 증가하는 부분 수열인 seq = [4, 6(or 7), 9, 10]을 구하기
"""

# S[start]에서 시작하는 증가 부분 수열 중 최대 길이를 반환해서 choices에 저장한다.
def lis4(start):
    if cache[start+1] != -1:
        return cache[start+1]
    
    cache[start + 1] = 1 # 항상 S[start]는 있기 때문에 길이는 1
    bestNext = -1

    # 최대 증가 부분 수열의 길이 구하기
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            cand = lis4(next) + 1

            # 재귀 호출을 통해 기존에 cache에 저장된 값보다 부분 수열의 길이가 긴 경우를 발견하면 cache 갱신
            if cand > cache[start + 1]:
                cache[start + 1] = cand
                bestNext = next # 어떤 숫자를 다음 숫자로 선택해야 전체 증가 부분 수열의 길이를 최대화 할지 저장
    
    choices[start + 1] = bestNext # choices에 이를 기록하고 이후에 실제 원소들을 나열할 때 사용
    return cache[start + 1]

# 최대 길이의 증가하는 부분 수열의 원소들을 구하는 함수
# 해당 원소를 seq 리스트에 저장함
def reconstruct(start, seq):
    if start != -1:
        seq.append(S[start])
    
    next = choices[start + 1]

    if next != -1:
        reconstruct(next, seq)

cache = [-1] * 101
S = [4, 7, 6, 9, 8, 10]
n = len(S)
choices = [-1] * 101
seq = []

lis4(-1)
reconstruct(-1, seq)
print(seq)