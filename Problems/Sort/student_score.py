n = int(input())

nameScores = {}


for i in range(n):
    name, score = input().split()
    nameScores[name] = int(score)

result = sorted(nameScores.items(), key=lambda x: x[1])

for key, value in result:
    print(key, end=' ')