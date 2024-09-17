function solution(my_string, queries) {
    var answer = [...my_string];

    for ([s, e] of queries) {
        let tmp = [...answer].slice(s, e+1).reverse();
        answer.splice(s, e-s+1, ...tmp);
    }
    return answer.join('');
}