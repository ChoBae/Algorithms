// 링크드 리스트는 꼬리랑 머리만 기억함
class Linklist {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  addToTail(value) {
    const curNode = new Node(value);
    if (!this.head) {
      this.head = curNode;
    }
    if (this.tail) {
      this.tail.next = curNode;
      curNode.prev = this.tail;
    }
    this.tail = curNode;
  }
  addToHead(value) {
    const curNode = new Node(value);
    if (this.head) {
      this.head.prev = curNode;
      curNode.next = this.head;
    }
    this.head = curNode;
  }
  removeHead() {
    if (!this.head) {
      console.log("머리가 없어요..");
      return;
    }
    const value = this.head.value;
    console.log("머리 댕겅 ~: ", this.head);
    if (this.head.next) {
      this.head = this.head.next;
    } else {
      // 다음이 없으면 하나남았다는거니까
      this.head = null;
      this.tail = null;

      return value;
    }
  }
  removeTail() {
    if (!this.tail) {
      console.log("링크드 리스트가 비어있어요");
      return;
    }
    const value = this.tail.value;
    console.log("꼬리 댕겅 ~: ", this.tail);
    if (this.tail.prev) {
      this.tail.prev.next = null;
      this.tail = this.tail.prev;
    } else {
      // 이전이 없으면 하나 밖에 없다는 뜻
      this.head = null;
      this.tail = null;
    }
    return value;
  }

  contain(target) {
    let cnt = 0;
    let curNode = this.head;
    let reverseNode = this.tail;
    while (curNode || reverseNode) {
      cnt++;
      if (curNode.value === target || reverseNode.value === target) {
        console.log(`찾았습니다.! ${cnt} 번의 횟수로 찾았어요.`);
        return true;
      }
      curNode = curNode.next;
      reverseNode = reverseNode.prev;
    }
    return false;
  }

  delete(value) {
    let curNode = this.head;
    while (curNode) {
      if (curNode.value === value) {
        curNode.next.prev = curNode.prev;
        curNode.prev.next = curNode.next;
        console.log("값을 찾았습니다.");
        break;
      }
      curNode = curNode.next;
    }
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

const L1 = new Linklist();
L1.addToTail(2);
// L1.removeHead()
L1.removeTail();
// L1.addToTail(3);
// L1.addToTail(4);
// L1.contain(4);
// L1.addToHead(1);
// L1.addToTail(5);
console.log(L1);
