// fuc fakeAPI
function fakeAPI(str) {
  // 문자가 아닐때 -1 반환
  if (typeof str !== "string") return Promise.reject(-1);
  return new Promise((resolve, reject) => {
    // 2초 delay check!
    // str의 길이를 반환.
    setTimeout(() => {
      resolve(str.length);
    }, 2000);
  });
}
// fuc iterableCall
function iterableCall(arr) {
  return new Promise((resolve, reject) => {
    const promises = arr.map((str) => fakeAPI(str));
    // all일시에는 하나가 reject시 거부됨. 만약 응답이 거절되어도 받을 수 있는 allSettled가 적합할듯(호환성 이슈는 존재함)
    //     Promise.all(promises).then((res) => {
    //       //console.log(res)
    //       resolve(res);
    //     });
    //   });
    Promise.allSettled(promises).then((res) => {
      // allSettled는 value, status를 가지고 있어서 value만 추출해주고, status가 rejected인 경우는 -1로 대체
      res = res.map((value) => (value === undefined ? -1 : value));
      resolve(res);
    });
  });
}
// fakeAPI(1)
// console.log(iterableCall(["hello", "KRAFton", "PUBG"]));
