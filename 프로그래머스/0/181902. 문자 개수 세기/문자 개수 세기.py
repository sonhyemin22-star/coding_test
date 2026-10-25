alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def solution(my_string):
    answer = []
    for text in alp:
        answer.append(my_string.count(text))
    return answer