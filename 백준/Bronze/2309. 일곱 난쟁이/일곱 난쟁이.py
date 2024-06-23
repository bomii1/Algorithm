heights = []
heightSum = 0
for i in range(9):
    height = int(input())
    heights.append(height)
    heightSum += height

heights = sorted(heights)
num = heightSum-100
x, y = 0, 0

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if heights[i] + heights[j] == num:
            x = i
            y = j
            break

for i in range(len(heights)):
    if i != x and i != y:
        print(heights[i])