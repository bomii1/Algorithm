let fs = require('fs');
let input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()

const queue = [];

queue.push(input);

for (let i=input-1; i>0; i--) {
    queue.unshift(i);

    for (let j=0; j<i; j++) {
        queue.unshift(queue.pop())
    }
}

console.log(queue.join(' '));