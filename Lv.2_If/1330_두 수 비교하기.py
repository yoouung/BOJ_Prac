# if문 뒤에 괄호 필요x

a, b = map(int, input().split(" "))

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")


