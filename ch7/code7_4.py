"""
7.1 예제 : 카라츠바의 빠른 정수 곱셈 알고리즘
"""

from code7_3 import normalize, multiply

# a, b : 정수의 리스트
# k : 정수

# a += b * (10 ** k)
def addTo(a, b, k):
    # 자리수 맞추기
    newsize = max(len(a), len(b) + k)

    # 동일한 자리수가 되도록 0추가
    while (len(a) != newsize):
        a.append(0)

    while (len(b) != newsize):
        b.append(0)

    # b의 최소 자리수부터 부터 더함
    for i in range(k, newsize):
        a[i] = a[i] + b[i - k]

    # 반올림 처리
    normalize(a)

# a -= b (a >= b를 가정함)
def subFrom(a, b):
    for i in range(len(b)):
        a[i] -= b[i]

    normalize(a)

def karatsuba(a, b):
    an = len(a)
    bn = len(b)

    # a가 b보다 짧은 경우 교체
    if an < bn:
        return karatsuba(b, a)

    # 기저 사례 1 : a나 b가 빈 리스트인 경우
    if an == 0 or bn == 0:
        return []

    # 기저 사례 2 : a가 비교적 짧은 경우 O(n^2) 곱셈으로 변경
    if an <= 2:
        return multiply(a, b)

    half = an // 2

    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(bn, half)]
    b1 = b[min(bn, half):]

    z0 = karatsuba(a0, b0)
    z2 = karatsuba(a1, b1)

    addTo(a0, a1, 0)
    addTo(b0, b1, 0)

    z1 = karatsuba(a0, b0)

    subFrom(z1, z0)
    subFrom(z1, z2)

    result = []
    addTo(result, z0, 0)
    addTo(result, z1, half)
    addTo(result, z2, 2*half)

    return result

print(karatsuba([4, 3, 2, 1], [9, 8, 7, 6, 5]))