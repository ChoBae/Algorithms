// Stone
function solution(H) {
  // 작으면 하나더 만들어져야함.
  let stack = [];
  let count = 0;
  for (let i = 0; i < H.length; i++) {
    while (stack.length > 0 && stack[stack.length - 1] > H[i]) {
      stack.pop();
    }
    if (stack.length === 0 || stack[stack.length - 1] < H[i]) {
      // console.log('if' ,stack[stack.length -1] )
      stack.push(H[i]);
      count++;
    }
  }
  return count;
}