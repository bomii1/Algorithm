function solution(array, commands) {
    let answer = [];

    commands.map(([i, j, k]) => {
        let num = array.slice(i-1, j).sort((a,b)=>a-b)[k-1];
        answer.push(num);
    })
    return answer;
}