"""
7.2 문제 : 쿼드 트리 뒤집기
- 난이도 : 하
- 쿼드 트리의 압축을 풀고 뒤집어 배열한 다음 쿼드 트리를 재구축하면 시간복잡도 초과
- 압축을 풀지 않고 뒤집는 방법을 사용하는 방법을 고안할 필요가 있음
"""

def reverse(quad, it):
    head = quad[it]
    it += 1

    # 기저 사례 : 구역이 완전한 흰색이나 검은색인 경우 뒤집어도 결과는 변하지 않는다.
    if head == 'w' or head == 'b':
        return head, it

    # 혼합 구역인 경우 4분면으로 나눠 뒤집는다.
    part_one, it = reverse(head, it) # 1사분면에 대한 뒤집기를 실행하고 인덱스 반환
    part_two, it = reverse(head, it) # 2사분면, 3사분면, 4사분면에 대해 동일하게 실행
    part_three, it = reverse(head, it)
    part_four, it = reverse(head, it)

    return 'x' + part_three + part_four + part_one + part_two, it # 뒤집힌 결과를 문자열로 만들어 인덱스와 함께 반환


for tc in range(int(input())):
    quad = input()

    print(reverse(quad, 0)[0])

