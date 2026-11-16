def solution(spell, dic):
    answer = []
    for word in dic:
        text = []
        for i in range(len(spell)):
            if spell[i] in word and word.count(spell[i]) == 1:
                text.append(1)
        answer.append(text)
    if [1] * len(spell) in answer:
        return 1
    return 2