# 소수점 반올림: round, 올림: math.ceil, 내림: math.floor
# -> round(숫자, 반올림자릿수)
# round 함수는 끝자리가 0이면 출력하지 않음

# format 메소드
# "{:.3f}".format(숫자)
# -> 끝자리가 0이어도 소수점 셋째자리 등등까지 표현 가능
# 문자열: %s, 정수 %d, 소수 %f, %.자릿수f
# https://dojang.io/mod/page/view.php?id=2300

# ------------------------------------------

C = int(input())

for i in range(C):
    # input = sys.stdin.readline().split(" ")
    # student_num = int(input[0])
    # => 처음부터 int값으로 받아야함(average도 int이어야하기 때문)
    nums = list(map(int, input().split(" ")))  # input은 변수명으로 x
    student_num = nums[0]
    s = []
    average = sum(nums[1:])/student_num

    for i in range(1, student_num+1):
        if nums[i] > average:
            s.append(nums[i])
    print("{:.3f}%" .format(len(s)/student_num*100))


    # # s라는 리스트를 안쓰고 count로도 쓸 수 있음
    # count = 0
    # for i in range(1, student_num+1):
    #     if nums[i] > average:
    #         count += 1
    # print("{:.3f}%".format(count/student_num*100))