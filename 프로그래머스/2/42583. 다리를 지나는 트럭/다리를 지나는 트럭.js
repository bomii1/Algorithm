function solution(bridge_length, weight, truck_weights) {
  let answer = 0;
  
  let bridge = new Array(bridge_length).fill(0);
  let curWeight = 0;
  
  answer++;
  bridge.shift();
  curWeight += truck_weights[0];
  bridge.push(truck_weights.shift());
  
  while (curWeight > 0) {
      answer++;
      curWeight -= bridge.shift();
      
      if (truck_weights.length > 0 && curWeight + truck_weights[0] <= weight) {
          curWeight += truck_weights[0];
          bridge.push(truck_weights.shift());
        } else {
          bridge.push(0);
      }
  }
  
  return answer;
}
