function solution(arr, queries) {
    queries.map(([s, e, k]) => {
        arr.slice(s, e+1).map((n, idx) => {
            if ((idx+s) % k == 0) {
                arr[idx+s] += 1
            }
        })
    })
    return arr;
}