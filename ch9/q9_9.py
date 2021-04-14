"""
9.9 문제 : 드래곤 커브
- 난이도 : 중
- 동적 계획법 테크닉
"""

# 2021/04/14

# 드래곤 커브 문자열을 생성하는 재귀 호출 알고리즘
# curve(seed, generations) = 초기 문자열 seed를 generations세대 진화시킨 결과를 반환
def curve(seed, generations):
    # 기저 사례 : 
    if generations == 0:
        print(seed)
        return

    for i in range(len(seed)):
        if seed[i] == 'X':
            curve("X+XF", generations-1)
        
        elif seed[i] == 'Y':
            curve("FX-Y", generations-1)
        
        else:
            print(seed[i])

# 드래곤 커브 문제를 해결하는 알고리즘

# xLength(n) = 문자열 "X"를 n세대 진화시킨 결과의 길이를 반환
# yLength(n) = 문자열 "Y"를 n세대 진화시킨 결과의 길이를 반환

# xLength(n) = xLength(n-1) + yLength(n-1) + 2
# yLength(n) = xLength(n-1) + yLength(n-1) + 2
# xLength(n) = yLength(n) = legnt(n) = 2 * length(n-1) + 2

MAX = int(1e9) + 1
EXPAND_X = "X+YF"
EXPAND_Y = "FX-Y"

# n 세대의 dragonCurve 문자열의 길이를 저장한다.
def precalc():
    length[0] = 1
    for i in range(1, 51):
        length[i] = min(MAX, length[i-1] * 2 + 2)
    
# dragonCurve를 generations 세대 진화시킨 결과에서 skip번째 문자를 반환한다.
def expand(dragonCurve, generations, skip):
    # 기저 사례
    # 재귀 호출을 모두 완료 했을 때 남아있는 skip보다 dragonCurve의 길이가 길어야 해당 dragonCurve 내에서 skip번째 이상의 문자열을 생성할 수 있다.
    if generations == 0:
        # 가정 설명문 assert 조건, (message): assert 뒤의 조건이 True가 아니면 (message와 함께) AssertError를 발생한다.
        # 단순히 에러를 찾는것이 아닌 실수를 가정하고 어떤 조건에 해당하는 값들을 보증하기 위한 '방어적 프로그래밍' 기법의 일종
        assert skip < len(dragonCurve)
        
        return dragonCurve[skip]

    for i in range(len(dragonCurve)):
        # 문자열이 X나 Y를 만나 확장(치환)되는 경우
        if dragonCurve[i] == 'X' or dragonCurve[i] == 'Y':
            # skip이 현재 세대의 드래곤 커브 문자열의 길이보다 크거나 길다면 skip에서 현재 드래곤 커브 문자열의 길이만큼 감소
            if skip >= length[generations]:
                skip -= length[generations]

            # skip이 현재 세대의 드래곤 커브 문자열의 길이보다 작다면 현재 세대의 문자열에서 p번째 문자를 찾을 수 있다는 의미
            # 현재 세대에 대한 드래곤 커브 문자열을 재귀적으로 만듦
            elif dragonCurve[i] == 'X':
                return expand(EXPAND_X, generations - 1, skip)

            else:
                return expand(EXPAND_Y, generations - 1, skip)

    
        # 확장(치환)되지는 않지만 건너뛰어야 할 경우
        # 문자열에서 F, -, +를 만나고 skip이 1이상이면 해당 문자를 건너뛴다는 의미
        elif skip > 0:
            skip -= 1

        # 답을 찾은 경우
        # skip == 0인 경우 해당 글자가 skip번째 문자가 된다.
        else:
            return dragonCurve[i]

    return '#' # 이 줄은 수행되지 않는다?

for tc in range(int(input())):
    n, p, l = map(int, input().split())
    
    length = [-1] * 51
    precalc()

    # expand 함수는 문자를 반환하기 위해 문제에서 원하는 문자열을 생성하기 위해서는 l번 반복해야 한다.
    # 문제에서 요구하는 p와 l은 1이상의 정수이기 때문에 실제 p번째 문자를 구하기 위해서는 p-1번째 문자를 출력해야 한다.
    for i in range(p, p+l):
        print(expand("FX", n, i-1), end = "")

    print()