const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const n = parseInt(input[0]);

const size = 100;
const paper = Array.from({ length: size }, () => Array(size).fill(0));

for (let i = 1; i <= n; i++) {
  const [x, y] = input[i].split(" ").map(Number);

  for (let row = x; row < x + 10; row++) {
    for (let col = y; col < y + 10; col++) {
      paper[row][col] = 1;
    }
  }
}

let totalArea = 0;
for (let row = 0; row < size; row++) {
  for (let col = 0; col < size; col++) {
    if (paper[row][col] === 1) {
      totalArea++;
    }
  }
}

console.log(totalArea);
