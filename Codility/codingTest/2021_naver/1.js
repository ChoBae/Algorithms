// 문자열 S와 배열 l
// 문자열 S의 문자들로 주어진 배열의 각 이름을 몇개나 만들 수 있을지 세어보고 최대 제작가능 횟수를 반환한다.
function solution(s, l) {
  // 알파벳 갯수 세기
  let dic = {};
  let answer = 0;
  let sLi = s.split("");
  for (let i = 0; i < sLi.length; i++) {
    if (dic[sLi[i]] === undefined) dic[sLi[i]] = 1;
    else dic[sLi[i]] += 1;
  }

  for (let i = 0; i < l.length; i++) {
    let wordDic = {};
    let curWord = l[i];
    let cnt = 999;
    for (let j = 0; j < curWord.length; j++) {
      if (wordDic[curWord[j]] === undefined) wordDic[curWord[j]] = 1;
      else wordDic[curWord[j]] += 1;
    }
    for (let [key, value] of Object.entries(wordDic)) {
      if (dic[key] === undefined) {
        cnt = 0;
        break;
      }
      cnt = Math.min(cnt, Math.floor(dic[key] / wordDic[key]));
    }
    console.log(cnt, curWord)
    answer = Math.max(answer, cnt);
  }
    console.log(answer)
}

solution("LILLYBILLYBOO", ["BILL", "MARIA", "LILLY"]);
