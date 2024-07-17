def func(n, start, end):
    if n == 1:
        arr[start][start] = 1
    else:
        for i in range(start, end+1):
            for j in range(start, end+1):
                if i == start or i == end:
                    arr[i][j] = 1
                else:
                    if j == start or j == end:
                        arr[i][j] = 1
        func(n-1, start+2, end-2)

n = int(input())
x = 4 * (n-1) + 1
arr = [[0] * x for _ in range(x)]
func(n, 0, 4*(n-1))

for i in range(x):
    for j in range(x):
        if arr[i][j]:
            print('*', end='')
        else:
            print(' ', end='')
    print()
