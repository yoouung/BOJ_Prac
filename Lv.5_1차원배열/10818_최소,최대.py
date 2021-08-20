# split이 리스트로 만들어주긴 하지만,,
# map을 통해 형변환 -> int (출력 시에 굳이 int()안붙이기 위해서)
# 이 때 map은 맵 객체를 만들기 때문에 list로 리스트형으로 바꿔줘야함

import sys

N = int(input())
nlist = list(map(int, sys.stdin.readline().split(" ")))

print(min(nlist), max(nlist))