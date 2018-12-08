class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currNode):
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key, val, currNode.leftChild)
            else:
                currNode.leftChild = TreeNode(key, val, parent=currNode)
        elif key > currNode.key:
            if currNode.hasRightChild():
                self._put(key, val, currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key, val, parent=currNode)
        else:
            currNode.val = val

    def __setitem__(self, k, v):
        self.put(k,v)

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


