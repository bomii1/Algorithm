function solution(name, yearning, photo) {
    let answer = [];
    let scoreMap = {};

    name.forEach((name, idx) => {
        scoreMap[name] = yearning[idx];
    });

    for (element of photo) {
        let score = 0;
        element.map((name) => {
            const value = scoreMap[name];
            value ? score += value : null;
        })
        answer.push(score);
    }
    return answer;
}