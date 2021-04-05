"""
9.2 문제 : 여행 짐 싸기
- 동적 계획법 테크닉
- 난이도 : 중
- 시간 복잡도
    * capacity의 범위는 [0, w], item의 인수의 범위는 최대 [0, n)
    * 존재하는 부분 문제의 수는 O(nw)
    * 각 부분 문제를 해결하는 시간은 상수 시간 O(1)
    * 결과적으로 nw * 1 이므로 전체 시간 복잡도는 O(nw)
"""

# 최대 절박도의 합을 반환
# pack(capacity, item) : 캐리어에 남은 용량이 capacity일 때, item 이후의 물건들을 담아 얻을 수 있는 최대 절박도의 합을 반환
def pack(capacity, item):
    # 기저 사례 : 더 이상 담을 수 있는 물건이 없을 때
    if item == n:
        return 0

    # 메모이제이션
    if cache[capacity][item] != -1:
        return cache[capacity][item]

    # 다음 물건을 담지 않을 경우
    cache[capacity][item] = pack(capacity, item + 1)

    # 다음 물건을 담을 경우
    # 남은 용량이 현재 담으려는 물건보다 커야 캐리어에 담을 수 있다.(조건문 빼먹는 실수)
    if capacity >= volume[item]:
        cache[capacity][item] = max(cache[capacity][item], pack(capacity - volume[item], item + 1) + need[item])

    return cache[capacity][item]

# 선택한 물품들을 역 추적하기
def reconstruct(capacity, item, picked):
    # 기저 사례 : 모든 물건들을 모두 고려함
    if item == n:
        return
    
    # 만일, 두 값이 같다면 items[item]은 선택하지 않았다는 의미이다.
    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item + 1, picked)

    # 두 값이 같지 않다면 items[item]은 선택했으므로 picked 리스트에 추가하고 다시 재귀적으로 다른 물건을 찾는다.
    else:
        picked.append(items[item])
        reconstruct(capacity - volume[item], item + 1, picked)
    


for tc in range(int(input())):
    n, w = map(int, input().split())

    items = []
    volume = []
    need = []
    for _ in range(n):
        name, vol, nd = input().split()
        items.append(name)
        volume.append(int(vol))
        need.append(int(nd))

    cache = [[-1] * len(items) for _ in range(w + 1)]
    picked = []

    reconstruct(w, 0, picked)

    import pprint
    pprint.pprint(cache)

    for p in picked:
        print(p)