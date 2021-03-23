"""
8.12 문제 : 비대칭 타일링
- 난이도 : 하
- 시간 복잡도 : O(n)
"""

# 전체 타일링하는 경우의 수에서 대칭 형태가 나타나는 경우의 수를 뺀다!
# 2*n 크기의 사각형에 대해서 n이 홀 수 일때는 한 가지(중앙에 세로 막대 1개),
# n이 짝 수 일때 나타나는 대칭형 타일의 두 가지 경우(중앙에 가로 막대 2개 or 완전 대칭)를 생각한다.

MOD = 1000000007

# 전체 타일링하는 경우의 수를 반환
def tiling(width):
    # 기저 사례 : width가 1 이하
    if width <= 1:
        return 1

    # 메모이제이션
    if cache[width] != -1:
        return cache[width]

    cache[width] = tiling(width - 1) + tiling(width - 2) % MOD
    return cache[width]

# 2 * width 크기의 사각형을 채우는 비대칭 방법의 수를 반환
def asymmetric(width):
    # width가 홀수인 경우
    if width % 2 == 1:
        # 전체 타일링하는 값에서 홀수인 경우 대칭 형태는 1가지만 고려하면 되기 때문에
        # 절반의 크기에 대해서 타일링한 결과만 빼주면 된다.
        # tiling의 반환값이 경우의 수가 아니라 MOD로 나눈 값이기 때문에
        # 결과를 구하기 전 MOD를 미리 더하고 다시 MOD로 나눠야 한다.
        return (tiling(width) - tiling(int(width/2)) + MOD) % MOD

    # width가 짝수인 경우
    result = tiling(width) # 전체 경우의 수
    result = (result - tiling(int(width/2)) + MOD) % MOD # 완전 대칭인 경우를 제외
    result = (result - tiling(int(width/2) - 1) + MOD) % MOD # 중앙에 가로 막대가 2개인 경우를 제외

    return result

for tc in range(int(input())):
    n = int(input())

    cache = [-1] * 101
    print(asymmetric(n))