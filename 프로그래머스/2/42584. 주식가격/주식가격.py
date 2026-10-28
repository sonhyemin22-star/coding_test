def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range((i + 1), len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
        if len(answer) == i:
            answer.append(len(prices) - i - 1)
    return answer