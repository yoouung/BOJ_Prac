# 리스트 선언: a = [] 또는 a = list()
# 리스트 길이: len(a)

n = []
for i in range(9):
    n.append(int(input()))

print(max(n))
for i in range(len(n)):
    if max(n) == n[i]:
        print(i+1)