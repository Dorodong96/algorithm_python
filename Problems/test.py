def solution(n):
    answer = ''
    while n != 0:
        answer += str((n - 1) % 3)
        n = n // 3

    answer.replace('20', '4')
    answer.replace('1', '2')
    answer.replace('0', '1')
    print(answer)
    return answer

solution(3)