function solution(s) {
    let answer = s.split(' ');

    s.split(' ').map((word, idx) => {
        let new_word = '';
        if (word !== '') {
            let first = word[0];
            let sub = word.slice(1).toLowerCase();
            +word[0] ? null : first = word[0].toUpperCase();
            new_word = first + sub;
        }
        answer[idx] = new_word;
    });
    return answer.join(' ');
}