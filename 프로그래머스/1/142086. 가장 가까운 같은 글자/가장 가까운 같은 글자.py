def solution(s):
    answer = []
    dic = {}
    
    for index, char in enumerate(s):
        if char in dic:
            answer.append(index - dic[char])
        else:
            answer.append(-1)
        dic[char] = index
    
    return answer