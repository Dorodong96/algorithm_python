n = int(input())
count = 0
hour = 0
minute = 0
second = 0


while not(hour == n and minute == 59 and second == 59):
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
    if '3' in (str(hour) + str(minute) + str(second)):
        count += 1

print(count)
