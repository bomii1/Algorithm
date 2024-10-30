const fs = require('fs');
const [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i=0; i<n; i++) {
    let stack = [];
    let answer = 'YES';
    for (p of input[i]) {
        if (p == '(') {
            stack.push(p);
        } else {
            if (stack.length) {
                stack.pop();
            } else {
                answer = 'NO';
            }
        }
    }
    if (stack.length) {
        answer = 'NO';
    }
    console.log(answer);
}