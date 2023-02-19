// Brackets -> O(N)
function solution(S) {
  // Implement your solution here
  let stack = [];
  let answer = false;
  for (let i = 0; i < S.length; i++) {
    const curS = S[i];
    if (stack.length >= 1) {
      if (stack[stack.length - 1] === "{" && curS === "}") stack.pop();
      else if (stack[stack.length - 1] === "(" && curS === ")") stack.pop();
      else if (stack[stack.length - 1] === "[" && curS === "]") stack.pop();
      else stack.push(curS);
    } else stack.push(curS);
  }
  answer = stack.length === 0 ? 1 : 0;
  return answer;
}
