function solution(msg) {
  var answer = [];
  const dict = {}; // 빈 객체 생성
  // 기본 색인 번호 생성
  for (let c = "A".charCodeAt(); c <= "Z".charCodeAt(); c++) {
    dict[String.fromCharCode(c)] = c - "A".charCodeAt() + 1;
  }
  let nextNum = 27;
  // 본격적으로 탐색
  let check = Array(msg.length).fill(false); // 반복문 재끼기 위한
  for (let i = 0; i < msg.length; i++) {
    if (!check[i]) {
      let curWord = msg[i];
      let nextWord = curWord + "";
      for (let j = i + 1; j < msg.length; j++) {
        nextWord += msg[j];
        if (dict[nextWord] === undefined) break;
        else {
          check[j] = true;
          curWord = nextWord;
        }
      }
      // 다음것 까지 있는 경우를 찾아야함.
      // 현재 입력 출력
      answer.push(dict[curWord]);
      dict[nextWord] = nextNum++;
    }
  }

  return answer;
}
