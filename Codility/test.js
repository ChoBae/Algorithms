function solution(fees, records) {
const unsortedObj = { 5961: 146, "0148": 670, "0000": 334 };
const arr = Object.entries(unsortedObj);
arr.sort(([a], [b]) => Number(a) - Number(b));
console.log(arr)
const sortedObj = Object.fromEntries(arr);
console.log(sortedObj);

}

solution()