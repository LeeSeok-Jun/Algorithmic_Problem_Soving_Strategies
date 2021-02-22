"""
7.1 예제 : 수열의 빠른 함과 행렬의 빠른 제곱
- fastsum(n) = 2 * fastsum(n/2) + n^2 / 4 (단, n은 짝수)
- 시간 복잡도 : O(logN)
"""

def fastsum(n):
    # 기저 사례 1 : n == 1
    if n == 1:
        return 1
    
    # 기저 사례 2 : n이 홀수
    if n % 2 == 1:
        return fastsum(n-1) + n

    return 2 * fastsum(n/2) + (n / 2) * (n / 2)

print(fastsum(10))
print(fastsum(11))

