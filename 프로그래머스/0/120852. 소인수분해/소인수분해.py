def solution(n):
    answer = []
    num = 2
    while num <= n:
        if n % num == 0:
            n //= num
            if not num in answer:
                answer.append(num)
        else:
            num += 1
    return answer