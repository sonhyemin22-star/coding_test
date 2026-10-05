def solution(myString):
    str_arr = myString.split('x')
    answer = []
    for text in str_arr:
        if text != '':
            answer.append(text)
    n = len(answer)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if answer[j] > answer[j + 1]:
                answer[j], answer[j + 1] = answer[j + 1], answer[j]
    return answer