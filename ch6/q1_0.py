"""
6.3 문제 : 소풍
- 난이도 : 하
- 답안 수의 상안은 모든 인원이 친구 관계일 때이다.
"""

# 2021/02/10 15:33 ~ 15:59
# 친구 관계를 표시하는 2차원 배열과 현재 짝이 맺어졌는지 저장하는 배열을 활용할 필요가 있다.

def countParings(taken):
    firstFree = -1 # 남은 학생 중 가장 번호가 빠른 학생을 찾기위한 변수

    for i in range(n):
        if taken[i] == False:
            firstFree = i
            break

    # 기저 사례 : 모든 학생이 짝을 이루면 종료
    if firstFree == -1:
        return 1

    result = 0
    # 가장 번호가 빠른 학생의 짝을 매칭함
    for next in range(firstFree + 1, n):
        # 다음에 나오는 사람 중 친구 관계이면서 아직 짝을 이루지 못 했다면 짝으로 연결
        if not taken[next] and areFriends[firstFree][next]:
            taken[firstFree] = True
            taken[next] = True
            result += countParings(taken) # 재귀 호출로 결과 누적

            # 다른 짝이 생길 수 있는 경우를 계산하기 위해 짝 관계를 해제
            taken[firstFree] = False
            taken[next] = False

    return result


for tc in range(int(input())):
    n, m = map(int, input().split())
    
    taken = [False] * n # 현재 짝이 맺어져있는지 정보를 저장
    areFriends = [[False] * n for _ in range(n)] # 친구 관계를 저장
    for i in range(m):
        a, b = map(int, input().split())
        areFriends[a][b] = True
        areFriends[b][a] = True

    print(countParings(taken))
    

    