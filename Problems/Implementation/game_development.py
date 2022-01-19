n, m = map(int, input().split())
a, b, direction = map(int, input().split())
map_matrix = [list(map(int, input().split())) for i in range(n)]

# 각 방향 (0, 1, 2, 3)에 대한 왼쪽 이동 좌표
direction_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]

count = 0
direction_count = [] # 주변 좌표 담기

while True:
    # 왼쪽 이동 방향
    xd = direction_list[direction][0]
    yd = direction_list[direction][1]

    # 1. 방문하지 않은 육지인 경우
    if map_matrix[a + xd][b + yd] == 0:
        # turn and move
        a += xd
        b += yd
        direction = (direction - 1) % 4  # 왼쪽으로 회전
        map_matrix[a][b] = 2  # 방문 표시를 2로 함.

        count += 1
        direction_count = []  # 주변 좌표 초기화

    # 2. 바다인 경우
    elif map_matrix[a + xd][b + yd] == 1:  # sea
        # just turn left
        direction = (direction - 1) % 4
        direction_count.append(1)

    # 3. 방문한 육지인 경우
    elif map_matrix[a + xd][b + yd] == 2:  # gone
        # just turn left
        direction = (direction - 1) % 4
        direction_count.append(2)
    # print(direction_count)

    if len(direction_count) == 4:  # 주변 좌표가 모두 0이 아닌 경우
        if direction_count[1] == 1:  # 한 칸 뒤가 1(바다)인 경우
            break
        elif direction_count[1] == 2:  # 한 칸 뒤가 2(방문한 육지)인 경우
            # 방향 유지 한 채로 한 칸 뒤로 이동 -> 왼쪽 회전 후 direction_list 참조(이동) 후 오른쪽 회전
            direction = (direction - 1) % 4
            a += direction_list[direction][0]
            b += direction_list[direction][1]
            direction = (direction + 1) % 4
            direction_count = []

    # print(map_matrix)


print(count)
