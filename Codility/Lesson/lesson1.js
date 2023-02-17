// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    // Implement your solution here
    // 숫자 -> 2진수
    // 최대 32개라서 괜찮을듯?
    let answer = -1
    let bin = N.toString(2);
    let isGapOpened = false
    let gapLength = 0

    for (let i = 0; i < bin.length; i++){
        // console.log(bin[i])
        if (bin[i] === '1'){
            if (answer < gapLength) answer = gapLength
            gapLength = 0
            isGapOpened = true
        }

        if (isGapOpened && bin[i] === '0' ){
            gapLength++
        }
    }
    // console.log(answer)
    return answer
}