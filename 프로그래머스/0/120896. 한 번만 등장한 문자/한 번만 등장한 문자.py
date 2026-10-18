def solution(s):
    answer = []
    for text in set(s):
        if s.count(text) == 1:
            answer.append(text)
    return ''.join(sorted(answer))