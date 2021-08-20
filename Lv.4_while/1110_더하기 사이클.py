# 생각 많이 많이,, 몰라서 답지 찾아봤따
# =아니고 ==인거 자꾸 까먹지 말기,,,

N = int(input())
a = N
new_a = 0
count = 0

while True:
    # 10보다 작아도 값은 동일하게 계산되므로 무시해도 된다.
    # if a < 10:
    #     new_a = a
    new_a = (a // 10) + (a % 10)
    a = (a % 10) * 10 + (new_a % 10)
    count += 1
    if a == N:
        break
print(count)