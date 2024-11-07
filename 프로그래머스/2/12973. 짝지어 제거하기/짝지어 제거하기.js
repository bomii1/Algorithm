function solution(s)
{
    let statk = [];
        
    if (s.length % 2 !== 0) return 0;
    
    for (let i=0; i<s.length; i++) {
        if (statk[statk.length-1] === s[i]) {
            statk.pop();
        }
        else {
            statk.push(s[i]);
        }
    }

    return statk.length ? 0 : 1;
}
