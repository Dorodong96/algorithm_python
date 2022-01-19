start = input()
x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = x_list.index(start[0]) + 1
y = int(start[1])
count = 0
x_move_list = [2, 2, -2, -2, 1, 1, -1, -1]
y_move_list = [1, -1, 1, -1, 2, -2, 2, -2]

for xm, ym in zip(x_move_list, y_move_list):
    x_move = x + xm
    y_move = y + ym
    if (1 <= x_move <= 8) and (1 <= y_move <= 8):
        count += 1

print(count)


