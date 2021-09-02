num = int(input())
count = 0


def han(n):
    if len(n) == 1 or len(n) == 2:   # 한자리, 두자리 수라면 참 반환
        return 0
    elif len(n) == 4:
        return 1
    elif n[2] - n[1] == n[1] - n[0]:
        return 0
    else:
        return 1


for N in range(1, num+1):
    num_list = list(map(int, str(N)))
    if han(num_list) == 0:
        count += 1

print(count)