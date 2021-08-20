# True -> T 무조건 대문자
# test개수가 정해지지 않음
# -> try, except로 int가 아닌 경우 break하게 하기

# 10951
while True:
    try:
        A, B = map(int, input().split(" "))
        print(A+B)
    except:
        break

# 10952
while True:
    A, B = map(int, input().split(" "))
    if A==0 & B==0:
        break
    print(A+B)
