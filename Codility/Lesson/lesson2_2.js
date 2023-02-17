// OddOccurrencesInArray
function solution(A) {
  // 중복 없는 수 찾기. 갯수 세서 홀수 갯수 내보내면.. log(N)
  let dic = {};
  for (let i = 0; i < A.length; i++) {
    if (dic[A[i]] === undefined) dic[A[i]] = 1;
    else dic[A[i]] += 1;
  }
  for (const [key, value] of Object.entries(dic)) {
    // console.log(key)
    if (value % 2 !== 0) return Number(key);
  }
}