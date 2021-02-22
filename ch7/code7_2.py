"""
7.1 예제 : 행렬의 거듭 제곱
"""

def pow(a, m):
    # 기저 사례 1: A^0 == 1
    if m == 0:
        return 1
    
    # m이 홀수인 경우
    if m % 2 > 0:
        return pow(a, m-1) * a

    half = pow(a, m / 2)

    return half * half

print(pow(4, 31))