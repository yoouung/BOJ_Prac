# (전체) - (생성자가 있는 숫자들) = (셀프 넘버 수)

# 집합(set) 활용
# 집합 값 1개 추가: a.add()
#     값 여러개 추가: a.update()

# 각 자릿수 합 구하기
# sum(map(int, str(n)))


Union = set(range(1, 10001))  # 범위로 집합 설정
num = set()
self_num = set()

def d(n):
    return n + (n // 1000) + (n // 100 - n//1000*10) + (n // 10 - n//100*10) + (n % 10)
# 처음에 n을 int로 안받고 문자열로 인식 후 자릿수 더하기 가능
# n(i)

for i in range(1, 10000):
    num.add(d(i))  # 10000까지의 숫자들로 다음 수 만들어서 집합
self_num = sorted(list(Union - num))  # 요소 하나하나 출력하기 위해서 리스트형으로 변환
                                      # 집합은 순서가 없음->sorted로 정렬
for i in range(len(self_num)):
    print(self_num[i])




# # 함수 안쓴 예시
    # for i in range(1, 10000):
    #     for j in str(i):
    #         d = i + int(j)
    #     num.add(d)
    #
    # self_num = sorted(Union - num)
    # for i in self_num:
    #     print(i)


# # 또는
    # # 함수 d 구현하기
    # def d(n):
    #     n = n + sum(map(int, str(n)))
    #
    #     return n
    #
    #
    # # 생성자가 있는지 확인할 리스트 초기화하기
    # a = [0] * 10001
    #
    # # 생성자 찾기
    # for i in range(1, 10001):
    #     a[i] = d(i)
    #
    # for i in range(1, 10001):
    #     # 셀프넘버라면 출력하기
    #     if i not in a:
    #         print(i)