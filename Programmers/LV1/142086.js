// 가장 가까운 글자
function solution(s) {
  let dic = {};
  let answer = [];
  for (let i = 0; i < s.length; i++) {
    let curWord = s[i];
    if (dic[curWord] === undefined) {
      dic[curWord] = i;
      answer.push(-1);
    } else {
      answer.push(i - dic[curWord]);
      dic[curWord] = i;
    }
  }
  return answer;
}