N, M, K = map(int, input().split())
list_num = list(map(int, input().split()))

list_num.sort()
answer = 0

''' 
for i in range(1, M+1):
    if i % K != 0:
        answer += list_num[-1]
    else:
        answer += list_num[-2]
'''

first = list_num[-1]
second = list_num[-2]

# 가장 큰 수가 더해지는 횟수
count = int(M / (K+1)) * K
count += M % (K+1)

answer += count * first
answer += (M - count) * second

print(answer)
