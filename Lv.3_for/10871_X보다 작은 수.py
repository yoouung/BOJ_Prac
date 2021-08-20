# 생각 많이 하게 됐던 문제

import sys

N, X = map(int, input().split(" "))
A = sys.stdin.readline().split(" ") # 자동으로 리스트로 저장됨

for j in range(N):
    if int(A[j]) < X:   # 리스트 안의 값은 문자열->int형으로 바꿈
        print(A[j], end=" ")  # 공백으로 이어서 출력: end=" "