def solution(s):
    answer = 0
    xcnt, cnt = 0, 0
    x = s[0]
    for i in range(len(s)):
        if x == s[i]:
            xcnt += 1
        else:
            cnt += 1
        if xcnt == cnt:
            answer += 1
            xcnt, cnt = 0, 0
            if i != len(s) - 1:
                x = s[i+1]
    if cnt != xcnt:
        answer += 1

    return answer