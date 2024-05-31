def solution(numbers):
    answer = [-1]*len(numbers)
    
    stack = []
    
    for index in range(len(numbers)):
    
        visit = numbers[index]
        
        while stack and numbers[stack[-1]]<visit:
            answer[stack.pop()]=visit
            
        stack.append(index)
                
    return answer