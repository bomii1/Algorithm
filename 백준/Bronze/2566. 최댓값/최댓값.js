const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

let max = 0;
let column = 0;
let row = 0;

for (let i=0; i<9; i++) {
    let rowMax = Math.max(...input[i])
    if (max <= rowMax) {
        max = rowMax;
        
        for (let j=0; j<9; j++) {
            if (input[i][j] === max) {
                column = j+1;
                row = i+1;
            }
        }
    }
}

console.log(max);
console.log(row, column);