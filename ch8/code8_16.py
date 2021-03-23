"""
8.11 예제 : 타일링 방법의 수 세기
- 난이도 : 하
- 부분 문제의 수는 O(n)이고 각각의 값을 계산하는데 O(1)의 시간이 들기 때문에
- 시간 복잡도 : O(n)
"""

# 부분 문제 정의하기
# tiling(n) = 2 * n 크기의 사각형을 2*1 크기의 타일로 덮는 방법을 의미
# 위 함수가 한 번 호출될 때 할 수 있는 선택은 세로 타일 하나를 쓰냐, 가로 타일 두 개를 쓰냐로 나뉜다.
# 점화식 tiling(n) = tiling(n - 1) + tiling(n - 2)


# n = 100이면 64bit 정수형 표현 범위도 훌쩍 넘어가기 때문에 MOD로 나눈 값을 반환하기로 함
MOD = 1000000007

cache = [-1] * 101

def tiling(width):
    # 기저 사례 : width가 1 이하
    if width <= 1:
        return 1

    # 메모이제이션
    if cache[width] != -1:
        return cache[width]

    cache[width] = (tiling(width - 1) + tiling(width - 2)) % MOD
    return cache[width]

print(tiling(100))