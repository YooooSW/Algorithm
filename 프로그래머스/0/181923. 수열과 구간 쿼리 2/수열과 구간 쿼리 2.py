def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        list = []
        
        for i in range(s, e+1):
            if arr[i] > k:
                list.append(arr[i])
        if list:
            answer.append(min(list))
        else:
            answer.append(-1)
            
    return answer

