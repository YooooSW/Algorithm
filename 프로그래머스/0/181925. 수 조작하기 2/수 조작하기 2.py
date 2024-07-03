def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        str = numLog[i] - numLog[i-1]
        
        if str == 1:
            answer += 'w'
        elif str == -1:
            answer += 's'
        elif str == 10:
            answer += 'd'
        elif str == -10:
            answer += 'a'
    return answer