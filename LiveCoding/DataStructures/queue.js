// // 링크드 리스트로 구현하기
// class Queue {
//   constructor() {
//     this.head = null;
//     this.tail = null;
//   }

//   append(value) {
//     const curNode = new Node(value);
//     if (!this.head) {
//       this.head = curNode;
//     }
//     if (this.tail) {
//       this.tail.next = curNode;
//     }
//     this.tail = curNode;
//   }
//   popleft() {
//     if (!this.head) return console.log("큐가 비었습니다.");
//     const targetValue = this.head;
//     if (this.head.next) this.head = this.head.next;
//     else this.head = null;
//     return targetValue.value;
//   }
//   appendleft(value) {
//     const curNode = new Node(value);
//     if (!this.head) this.head = curNode;
//     if (!this.tail) this.tail = curNode;
//     else if (this.tail && this.head) {
//       curNode.next = this.head;
//       this.head = curNode;
//     }
//   }
// }

// class Node {
//   constructor(value) {
//     this.value = value;
//     this.next = null;
//   }
// }

// const q = new Queue();
// // q.append(1);
// q.appendleft(2);
// // q.append(2);
// q.append(3);
// // console.log(q.popleft());
// console.log(q);

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }
  append(value) {
    const curNode = new Node(value);
    if (!this.head) {
      this.head = curNode;
      this.tail = curNode;
      return;
    } else {
      this.tail.next = curNode;
      curNode.prev = this.tail;
      this.tail = curNode;
    }
  }
  appendLeft(value) {
    const curNode = new Node(value);
    if (!this.head) {
      this.head = curNode;
      this.tail = curNode;
      return;
    } else {
      this.head.prev = curNode;
      curNode.next = this.head;
      this.head = curNode;
    }
  }
  popLeft() {
    if (!this.head) return console.log("큐가 비었습니다.");
    const value = this.head.value;
    this.head = this.head.next;
    this.head.prev = null;
    return value;
  }
  pop() {
    if (!this.tail) return console.log("큐가 비었습니다.");
    const value = this.tail.value;
    this.tail = this.tail.prev;
    this.tail.next = null;
    return value;
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

const q = new Queue();
q.append(1);
q.append(2);
q.append(3);
q.append(4);
q.appendLeft(0);
// console.log(q.popLeft());
// console.log(q.popLeft());
console.log(q.pop());
console.log(q);
