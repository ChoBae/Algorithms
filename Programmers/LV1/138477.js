function solution(k, score) {
  let answer = [];
  let stack = [];
  let minNum = Number.MAX_SAFE_INTEGER;
  for (let val of score) {
    let minStack = Math.min(...stack);

    if (stack.length >= k && minStack < val) {
      let delIdx = stack.indexOf(minStack);
      console.log(delIdx);
      stack.splice(delIdx, 1);
      stack.push(val);
    } else if (stack.length < k) {
      // 명예의 전당에 넣어주기
      stack.push(val);
    }

    answer.push(Math.min(...stack));
  }
  // 힙구조가 제일 편하겠다 쩝..
  return answer;
}
