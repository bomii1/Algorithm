function solution(ineq, eq, n, m) {
    var answer = 0;
    let x = ineq + eq;
    if (x === '<=') {
        answer = n <= m;
    } else if (x === '>=') {
        answer = n >= m;
    } else if (x === '<!') {
        answer = n < m;
    } else {
        answer = n > m;
    }
    return answer === true ? 1 : 0;
}