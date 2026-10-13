def solution(arr, flag):
    answer = []
    for num, bool in zip(arr, flag):
        if bool:
            answer.extend([num] * (num * 2))
        else:
            answer = answer[:(len(answer) - num)]
    return answer