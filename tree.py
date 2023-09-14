class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        s = f"{self.key}"
        if self.leftChild:
            s += f"[{str(self.leftChild)}]"
        else:
            s += "[]"

        if self.rightChild:
            s += f"[{str(self.rightChild)}]"
        else:
            s += "[]"

        return s


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    assert str(r) == 'a[][]'

    r.insertLeft('b')
    r.insertRight('c')
    print(r)
    assert str(r) == 'a[b[][]][c[][]]'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    print(r)
    assert str(r) == 'a[b[d[][]][e[][]]][c[f[][]][]]'
    print(r.getRootVal())
    assert r.getRootVal() == 'a'
    print(r.getLeftChild())
    assert str(r.getLeftChild()) == 'b[d[][]][e[][]]'
    print(r.getRightChild())
    assert str(r.getRightChild()) == 'c[f[][]][]'
