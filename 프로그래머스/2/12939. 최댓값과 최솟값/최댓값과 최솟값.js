function solution(s) {
    let answer = '';
    let arr = s.split(' ').sort((a,b)=>a-b);
    return `${Math.min(...arr)} ${Math.max(...arr)}`
}