let fs = require('fs');
let input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split('\n')
    .map(line => line.split(' ').map(Number));

let xArr = input.map(point => point[0]).sort((a, b) => a - b);
let yArr = input.map(point => point[1]).sort((a, b) => a - b);

let answer = [
    xArr[0] === xArr[1] ? xArr[2] : xArr[0],
    yArr[0] === yArr[1] ? yArr[2] : yArr[0]
];

console.log(answer[0], answer[1]);
