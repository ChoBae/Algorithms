// 튜플
function solution(s) {
  var answer = [];
  let obj = {};
  var supers = s.split(",");
  const regex = /[^0-9]/g;
  for (let i = 0; i < supers.length; i++) {
    const res = supers[i].replace(regex, "");
    if (obj[res] === undefined) obj[res] = 1;
    else {
      obj[res] += 1;
    }
  }

  const keys = Object.entries(obj)
    .sort((a, b) => b[1] - a[1])
    .map(([key, value]) => parseInt(key, 10));
  console.log(keys);
  return keys;
}