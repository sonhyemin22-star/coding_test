def solution(my_strings, parts):
    new_parts = []
    for i in range(len(parts)):
        new_parts.append([parts[i][0], parts[i][1] + 1])
    answer = ''
    for text, num in zip(my_strings, new_parts):
        answer += text[num[0]:num[1]]
    return answer