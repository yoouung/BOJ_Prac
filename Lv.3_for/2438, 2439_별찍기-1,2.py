# 2438
# aaa = "a"*3
N = int(input())

for i in range(N):
    print("*" * (i+1))


# 2439
# 콤마, 사용해서 값들을 이어서 출력하면 공백 추가
# 덧셈+ 사용하면 공백 추가x
N = int(input())

for i in range(1, N+1):
    print(" "*(N-i) + "*"*i)