class QueueWithStack {
  constructor() {
    this.stackNewest = new Stack();
    this.stackOldest = new Stack();
  }
  add(value) {
    this.stackNewest.push(value);
  }
  shiftStacks() {
    if (this.stackOldest.isEmpty()) {
      while (!this.stackNewest.isEmpty()) {
        this.stackOldest.push(this.stackNewest.pop());
      }
    }
  }
  remove() {
    if (this.stackNewest.isEmpty()) return console.log("큐가 비어있음");
    this.shiftStacks();
    const value = this.stackOldest.pop();
    while (!this.stackOldest.isEmpty()) {
      this.stackNewest.push(this.stackOldest.pop());
    }
    return value;
  }
}

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

// const stack = new Stack();
// stack.push(1);
// stack.push(2);
// stack.push(3);
// stack.push(4);
// console.log(stack.pop());
// console.log(stack.pop());
// console.log(stack.pop());
// console.log(stack.pop());
// console.log(stack.pop());
// console.log(stack);

const test = new QueueWithStack();
test.add(1);
test.add(2);
test.add(3);
console.log(test.remove());
console.log(test.remove());
console.log(test.remove());
console.log(test);
