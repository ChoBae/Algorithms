function solution(S) {
  // Implement your solution here
  // 정규 표현식
  const wordLi = S.split(" ");
  const allCheck = /^[a-zA-Z0-9]*$/;
  const alpCheck = /[0-9]/g;
  let answer = -1;
  for (let word of wordLi) {
    if (allCheck.test(word)) {
      let len = word.length;
      let alpPass = word.replace(alpCheck, "").length % 2 == 0;
      let oddPass = len % 2 !== 0;
      if (alpPass && oddPass && answer < len) answer = len;
    }
  }
  return answer;
}
