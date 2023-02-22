// 영어 끝말잇기
// 한바퀴돌면 다시 첫사람으로
// 이전에 등장한 단어 사용 금지 (큐나 스택에서 빼야할듯)
// 한글자 안됨.
// 시간 복잡도 O(N)
function solution(n, words) {
  let answer = [0, 0];
  let status = new Set(); // 사용된 단어를 저장할 set
  let preWord = words[0]; // 이전 단어
  status.add(preWord);
  // 끝말잇기 시작
  for (let i = 1; i < words.length; i++) {
    let curWord = words[i]; // 현재 단어
    // 끝말 잇기가 성공했을때
    if (preWord[preWord.length - 1] === curWord[0]) {
      preWord = curWord; // 이전단어 업데이트
      // 만약 이전에 사용했다면 break
      if (!status.has(curWord)) status.add(curWord);
      else {
        answer = i + 1;
        break;
      }
    } else { // 끝말잇기가 틀렸을 때
      answer = i + 1;
      break;
    }
  }
  // 플레이어와 순서 찾기
  let playerNUm = (answer % n) - 1 < 0 ? n : answer % n;
  let seq = Math.ceil(answer / n);
  if (playerNUm && seq) answer = [playerNUm, seq];
  return answer;
}
