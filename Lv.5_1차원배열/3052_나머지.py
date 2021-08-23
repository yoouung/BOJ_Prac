# 리스트 중복 제거: set()
# ex) a = set(list)        -> 순서가 뒤죽박죽 될 수 있음
# 순서가 중요하다면:
# for a in list:
#   if a not in new_list:
#       new_list.append(a)

nums = [] # for문 안 말고 먼저 선언해주기
remains = []

for i in range(10):
    num = int(input())
    nums.append(num)
    remain = num%42
    remains.append(remain)

remains = set(remains) # 중복 제거
# 필요없었던 코드였던 것...
# remains = list(remains) # 다시 리스트로 변환
print(len(remains))


# 간단명료한 코드
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))