function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[Math.floor(arr.length / 2)];
  const less = [];
  const equal = [];
  const greater = [];

  for (let element of arr) {
    if (element < pivot) {
      less.push(element);
    } else if (element === pivot) {
      equal.push(element);
    } else {
      greater.push(element);
    }
  }

  let lessArr = quickSort(less);
  let greaterArr = quickSort(greater);
  let newArr = [...lessArr, ...equal, ...greaterArr];
  return newArr;
}

// 퀵소트 예제 실행
const arr = [5, 2, 9, 1, 7, 6, 3, 8, 4];
const sortedArr = quickSort(arr);
console.log(sortedArr);
