n = int(input())

# 생성자
generator = 0

for i in range(1, n+1):
    arr = list(str(i))
    SUM = i
    for j in range(len(arr)):
        SUM += int(arr[j])
    if SUM == n:
        generator = i
        break
print(generator)