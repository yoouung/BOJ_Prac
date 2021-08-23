# 리스트에서 특정 요소 개수 구하기: 리스트.count(요소)
# ex) a.count(1)

# int to list:
# list(map(int, str(n))) 또는 [int(a) for a in str(숫자)]

a = int(input())
b = int(input())
c = int(input())

ans = a * b * c
ans_list = list(map(int, str(ans)))

for i in range(10):
    print(ans_list.count(i))
