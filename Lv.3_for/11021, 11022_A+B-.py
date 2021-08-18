# 11021 A+B-7
import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split(" "))
    sum = a + b
    print("Case #%d: %d" %(i+1, sum)) # ""뒤 , 없어야함
    # 그냥 "Case #" + i + 로 하면 띄어쓰기 무조건 포함
    # 그래서 %d 씀


# 11021 A+B
import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split(" "))
    sum = a + b
    print("Case #%d: %d + %d = %d" %(i+1, a, b, sum))
