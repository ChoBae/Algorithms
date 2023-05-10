class Stack {
  constructor() {
    this.top = null;
  }

  push(value) {
    const curNode = new Node(value);
    if (this.top) curNode.next = this.top;
    this.top = curNode;
  }
  pop() {
    if (!this.top) return console.log("스택이 비었어요.");
    const value = this.top.value;
    this.top = this.top.next;
    return value;
  }
  isEmpty() {
    return !this.top;
    // let node = this.top
    // while (node) {
    //     if ()
    // }
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack);

