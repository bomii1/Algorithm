function solution(num_list) {
    var answer = 0;
    let even = '';
    let odd = '';
    for (const num of num_list) {
        if (num % 2 === 0) {
            even += num;
        } else {
            odd += num;
        }
    }
    return parseInt(even) + parseInt(odd);
}