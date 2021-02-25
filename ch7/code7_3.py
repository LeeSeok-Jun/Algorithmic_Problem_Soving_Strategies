"""
7.1 예제 : 두 큰 수를 곱하는 O(n^2)시간 알고리즘
"""

# 자리수 올림을 처리하는 함수
def normalize(num):
    num.append(0)

    for i in range(len(num) - 1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10 # 괄호 실수
            num[i+1] -= borrow
            num[i] += borrow * 10 # 복합 대입 연산자 빼먹음

        else:
            num[i+1] += num[i] // 10
            num[i] %= 10

    while len(num) > 1 and num[len(num)-1] == 0:
        num.pop(len(num)-1)


# 두 자연수의 곱을 반환
# 각 배열에는 각 수의 자리수가 1의 자리에서부터 시작되 저장되어있음
# multiply([3, 2, 1], [6, 5, 4]) = 123*456을 의미
def multiply(a, b):
    # 책의 오타?
    # c = [0] * (len(a) + len(b) + 1)
    c = [0] * (len(a) + len(b) - 1)

    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]

    normalize(c)
    return c

# answer = multiply([3, 2, 1], [6, 5, 4])
# result = 0
# for i in range(len(answer)):
#     result += answer[i] * (10 ** i)

# print(result)