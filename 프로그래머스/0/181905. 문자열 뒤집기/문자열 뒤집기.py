def solution(my_string, s, e):
    text = my_string[s:(e + 1)][::-1]
    return my_string[:s] + text + my_string[(e + 1):]