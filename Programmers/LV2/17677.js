// 17677;
// 뉴스 클러스터링
function solution(str1, str2) {
  // 예외 처리(대소문자)
  str1 = str1.toUpperCase();
  str2 = str2.toUpperCase();
  let str1Dic = {};
  let str2Dic = {};
  // 1. 원소 구하기
  for (let i = 0; i < str1.length - 1; i++) {
    let curWord = str1[i] + str1[i + 1];
    curWord = curWord.match(/[a-zA-Z]+/g);
    if (curWord === null || curWord[0].length === 1) continue;
    if (str1Dic[curWord] === undefined) str1Dic[curWord] = 1;
    else str1Dic[curWord] += 1;
  }

  for (let i = 0; i < str2.length - 1; i++) {
    let curWord = str2[i] + str2[i + 1];
    curWord = curWord.match(/[a-zA-Z]+/g);
    if (curWord === null || curWord[0].length === 1) continue;
    if (str2Dic[curWord] === undefined) str2Dic[curWord] = 1;
    else str2Dic[curWord] += 1;
  }
  // 2. 교집합 차집합 구하기
  let 교집합 = 0;
  let 합집합 = 0;
  // 교집합
  for (let key in str1Dic) {
    if (str1Dic[key] !== undefined && str2Dic[key] !== undefined)
      교집합 += Math.min(str2Dic[key], str1Dic[key]);
  }
  // 합집합
  for (let key in str1Dic) {
    if (str2Dic[key] !== undefined && str2Dic[key] < str1Dic[key])
      str2Dic[key] = str1Dic[key];
    else if (str2Dic[key] === undefined) str2Dic[key] = str1Dic[key];
  }
  for (let key in str2Dic) {
    합집합 += str2Dic[key];
  }
  // 합집합(분모)이 0일때의 예외처리
  if (합집합 === 0) return 65536;
  let 자카드유사도 = 교집합 / 합집합;
  return Math.floor(자카드유사도 * 65536);
}
