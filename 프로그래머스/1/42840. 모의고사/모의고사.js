function solution(answers) {
    let answer = [];
    const stu1 = [1, 2, 3, 4, 5];
    const stu2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    let score1 = check(stu1, answers);
    let score2 = check(stu2, answers);
    let score3 = check(stu3, answers);
    console.log(score1, score2, score3);
    
    const highest = Math.max(score1, score2, score3);
    
    if (highest == score1) answer.push(1);
    if (highest == score2) answer.push(2)
    if (highest == score3) answer.push(3);
    
    return answer;
}

function check(stu, answers) {
    let score = 0;
    let cur = -1;

    for (let i=0; i<answers.length; i++) {
        if (cur == stu.length-1) {
            cur = -1;
        }
        cur += 1;
        if (stu[cur] == answers[i]) {
            score += 1;
        }
    }
    return score;
}