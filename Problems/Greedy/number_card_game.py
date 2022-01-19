rows, cols = map(int, input().split())
min_list = []
for r in range(rows):
    col = input().split()
    min_list.append(min(col))

print(max(min_list))