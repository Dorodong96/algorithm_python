n = int(input())
directions = input().split()

point = [1, 1]
for direction in directions:
    if direction == 'L' and point[1] > 1:
        point[1] -= 1
    elif direction == 'R' and point[1] < n:
        point[1] += 1
    elif direction == 'U' and point[0] > 1:
        point[0] -= 1
    elif direction == 'D' and point[0] < n:
        point[0] += 1

print("{} {}".format(point[0], point[1]))
