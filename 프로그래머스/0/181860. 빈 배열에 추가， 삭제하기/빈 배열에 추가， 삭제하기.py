def solution(arr, flag):
    answer = []
    for i, bool in enumerate(flag):
        if bool:
            answer.extend([arr[i]] * (arr[i] * 2))
        else:
            answer = answer[:(len(answer) - arr[i])]
    return answer