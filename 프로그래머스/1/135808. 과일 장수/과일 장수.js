function solution(k, m, score) {
    let answer = 0;
    let pre = 0;
    score = score.sort((a,b) => b-a);
    if (score.length >= m) {
        for (let i=m; i<=score.length; i+=m) {
            let box = score.slice(pre, i);
            answer += Math.min(...box) * m;
            pre += m;
        }
    }
    return answer;
}