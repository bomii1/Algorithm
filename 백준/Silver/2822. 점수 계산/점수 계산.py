scores = [0] * 8

for i in range(8):
  score = int(input())
  scores[i] = [i+1, score]

scores.sort(key=lambda x:x[1], reverse=True)
scoreSum = 0
scoreIndex = []
for i in range(5):
  scoreSum += scores[i][1]
  scoreIndex.append(scores[i][0])

scoreIndex.sort()
print(scoreSum)
print(*scoreIndex)
