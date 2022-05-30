a, b, c = map(int, input().split())
if a==b==c:
    m = 10000 + (a * 1000)
elif a==b or a==c:
    m = 1000 + (a * 100)
elif b==c:
    m = 1000 + (b * 100)
else:
    max=(a>b) and a or b    # a가 b보다 크면 max=a, a가b보다 크지않으면 max=b
    m=(c>max) and c or max  # c가 max보다 크면 max=c, c가max보다 크지 않으면 max=max
    m= 100 * m
print(m)