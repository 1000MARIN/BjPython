h,m = map(int,input().split())
l = int(input())
h+= l // 60
m+= l % 60
if m > 59:
    h += 1
    m -= 60
if h > 23:
    h -= 24
print(h,m)
