# 몰라서 검색해봤다
# O일때 score +1, count +1 해주고 score에 count도 더함

N = int(input())

for i in range(N):
    ans = input()  # 리스트로 선언+sys.stdin.readline 안하고
                   # 그냥 input으로 해도 되나봐!!!!
    score = 0      # ans별로 score 다르니까 for문안에 선언
    count = 0
    for j in range(len(ans)):
        if ans[j] == "O":
            score = score + 1 + count
            count += 1
        elif ans[j] == "X":     # x만나면 count는 0으로
            count = 0
    print(score)
