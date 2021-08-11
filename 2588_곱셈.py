a = int(input())
b = int(input())

c = a * (b - int(b // 10) * 10)
d = a * (int(b // 10) - int(b // 100) * 10)
e = a * (int(b // 100))
f = e * 100 + d * 10 + c

print(c)
print(d)
print(e)
print(f)
