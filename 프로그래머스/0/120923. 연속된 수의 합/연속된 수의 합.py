def solution(num, total):
    sum = 0
    answer = []
    for i in range(num):
        sum += i
    n = (total - sum) // num
    for i in range(num):
        answer.append(n + i)
    return answer