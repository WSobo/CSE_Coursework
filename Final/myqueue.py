from stack import Stack


class PriorityQueue:
    def __init__(self):
        self.stack = Stack()

    def __str__(self):
        return str(self.stack)

    def empty(self):
        return self.stack.isEmpty()

    def enqueue(self, item):
        if self.stack.isEmpty() or item < self.stack.peek():
            self.stack.push(item)
        else:
            # Pop the top item, recursively enqueue the new item, and then push the popped item back
            popped_item = self.stack.pop()
            self.enqueue(item)
            self.stack.push(popped_item)

    def dequeue(self):
        return self.stack.pop()


if __name__ == '__main__':
    pq = PriorityQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        pq.enqueue(i)
        print('adding', i)
        print(pq)

    while not pq.empty():
        print('removing', pq.dequeue())
        print(pq)
