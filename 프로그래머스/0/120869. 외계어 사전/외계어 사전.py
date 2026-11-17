def solution(spell, dic):
    answer = []
    for word in dic:
        text = []
        for alp in spell:
            if alp in word and word.count(alp) == 1:
                text.append(1)
        answer.append(text)
    if [1] * len(spell) in answer:
        return 1
    return 2