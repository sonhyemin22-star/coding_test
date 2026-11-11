def solution(numbers):
    answer = ''
    str_num = list(map(str, numbers))
    str_num.sort(reverse=True, key=lambda x : x * 3)
    for num in str_num:
        answer += num
    if str_num[0] == '0':
        return '0'
    return answer