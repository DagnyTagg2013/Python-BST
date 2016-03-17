class TreeNode:

    INVALID_PRECONDITION_TO_FIND_SUCCESSOR = "Invalid BST Node State to Find Successor";

    # NOTE:  - Python ctor support
    #        - has distinction between key and value
    #        - needs connection to PARENT to support delete
    #        - needs connection to left, right to support recursive navigation
    #        - essentially, pointers UP and DOWN tree from node need updating on a deletion
    #          SO, needs to know if it IS a left child, right child, leaf, root
    def __init__(self,key,value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return (not not self.leftChild)

    def hasRightChild(self):
        return (not not self.rightChild)

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # NOTE:  how this is determined through access to PARENT
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # NOTE how this is determined through access to PARENT, i.e. this node does NOT have a parent, OR can have None as parent
    def isRoot(self):
        return not self.parent

    # NOTE how this property is determined
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    # NOTE how this efficiently overwrites data in-place and reconnects associations efficiently
    """
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.isLeftChild():
            self.leftChild.parent = self
        if self.isRightChild():
            self.rightChild.parent = self
    """

    # NOTE:  - ITERABLE treenode is RECURSIVE in that __iter__ enables for .. in
    #        - It's recursive over TREENODE
    #        It provides for recursive BST property with INORDER traversal:
    #        L subtree; ROOT; R subtree
    #        i.e. RECURSIVELY iterate thru LEFT subtree, PRIOR to navigating RIGHT subtree
    #        YIELD is used to SAVE last-generated state to pickup on NEXT invocation
    # iterator method returns TUPLE key-value for root; otherwise yields next treeenode
    # def __iter__(self):
    # MISS-ATTENTION!!!  - __iter__() implementation CAN ONLY be invoked as follows:
    #                      for nextNode in aStruct_thathas__iter__() ...
    #                    - DIFFERENT from simple method invocation with RETURN value expected
    #                      with NO way to BREAK looping between yield calls!
    def __iter__(self):

        if self:
            if self.hasLeftChild():
                # RECURSE iteration within LEFT subtree
                for elem in self.leftChild:
                    yield elem
            yield self
            if self.hasRightChild():
                # RECURSE iteration within RIGHT subtree
                for elem in self.rightChild:
                    yield elem
        else:
            raise StopIteration("END of tree reached.")








