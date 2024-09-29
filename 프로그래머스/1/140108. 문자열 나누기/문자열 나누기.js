function solution(s) {
    let answer = 0;
    let cnt = 0;
    let cur = '';

    for (let i=0; i<s.length; i++) {
        if (cnt === 0) {
            cnt = 1;
            answer++;
            cur = s[i];
        } else {
            if (cur === s[i]) cnt++;
            else cnt--;
        }
    }
    return answer;
}