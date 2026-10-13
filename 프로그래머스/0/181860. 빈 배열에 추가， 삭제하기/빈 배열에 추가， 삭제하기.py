def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        x = []
        if flag[i] == True:
            x.append(arr[i])
            x = x * (arr[i] * 2)
            answer += x
        else:
            answer = answer[:(len(answer) - arr[i])]
    return answer