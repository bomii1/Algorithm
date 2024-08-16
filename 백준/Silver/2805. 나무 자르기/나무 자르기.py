import sys
input = sys.stdin.readline

n, m = map(int, input().split())
namu = list(map(int, input().split()))

start = 0
end = max(namu)

while start <= end:
    SUM = 0
    x = (start+end) // 2
    for e in namu:
        if e > x:
            SUM += e - x
    if SUM < m:
        end = x - 1
    else:
        start = x + 1
print(end)