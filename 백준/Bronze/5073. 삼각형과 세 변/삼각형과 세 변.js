let fs = require('fs');
let input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split('\n')
    .map(line => line.split(' ').map(Number));

for (let i=0; i<input.length-1; i++) {

    let temp = input[i].sort((a, b) => a - b);
    const x = temp[0];
    const y = temp[1];
    const z = temp[2];

    if (x + y <= z) {
        console.log('Invalid');
    } else {
        if (x === y && y === z && z === x) {
            console.log('Equilateral');
        } else if (x !== y && y !== z && z !== x) {
            console.log('Scalene');
        } else {
            console.log('Isosceles');
        }
    }
}