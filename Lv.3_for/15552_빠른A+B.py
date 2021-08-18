# input대신 sys.stdin.readline
# 맨끝의 개행문자까지 입력받음
# 문자열을 저장하고 싶은 경우 .rstrip()을 추가

import sys

T = int(input())
for i in range(T):
   a, b = map(int, sys.stdin.readline().split())
   print(a + b)
