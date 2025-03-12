let fs = require('fs');
let input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split('\n')

const stack = [];

for (let i=1; i<=input[0]; i++) {
    const temp = input[i].split(' ');
    const cmd = temp[0];

    if (temp.length > 1) {
        const num = temp[1];
        stack.push(num);
    } else {
        if (cmd === 'pop') {
            if (stack.length === 0) {
                console.log(-1);
            } else {
                console.log(stack.pop());
            }
        } else if (cmd === 'size') {
            console.log(stack.length);
        } else if (cmd === 'empty') {
            if (stack.length === 0) {
                console.log(1);
            } else {
                console.log(0);
            }
        } else if (cmd === 'top') {
            if (stack.length === 0) {
                console.log(-1)
            } else {
                console.log(stack[stack.length-1]);
            }
        }
    }
}