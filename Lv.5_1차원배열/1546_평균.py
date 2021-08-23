import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split(" ")))
sum = 0
max = max(scores) # for문 안에서 max가 바뀔 수 있으니 미리 선언

for i in range(N):
    scores[i] = scores[i]/max*100
    sum += scores[i]
print(sum/N)