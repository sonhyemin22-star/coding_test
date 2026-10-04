def solution(num_list, n):
    answer = []
    i = 0
    while i < len(num_list):
        num = num_list[i]
        answer.append(num)
        i += n
    return answer