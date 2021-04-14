visited = 0b1000
for next in range(4):
    print(visited, 1<<next, visited & 1<<next)
    
    if visited & ~(1<<next):
        print(next, "에 이미 방문했어요")
    else:
        print(next, "에 아직 방문하지 않았어요")

print(visited + 1<<0)
print(bin(visited + 1<<0))