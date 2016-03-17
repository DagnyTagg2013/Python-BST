
from BST.treenode import TreeNode
from BST.bstIterator import BSTiterator

# TODO:  import this to support breadth-first search!
# from collections import deque

# TODO:  handle insertion of duplicate key case!

"""

BST PROPERTY:
- ROOT
- all keys within LEFT subtree are LESS than key on root
- all keys within RIGHT subtree are GREATER than key on root
= holds for roots of each subtree, recursively
- TODO:  ASSUMEs no DUPLICATEs (check for EQUALs on INSERT, and throw EXCEPTION)

CAVEAT:  NOT sufficient to check that within ONE given level; this property holds, for successive levels
This instead must hold ACROSS ALL levels for left and right subtrees:
eg the following is not a BST since 4 > 3.

            3
           / \
          2   5
         / \
        1   4

SO MAX key in left subtree is < root
AND MIN key in right subtree is > root

IMPLEMENTATION:
- BinarySearchTree (maybe empty, so want separate class, TreeNode)
- TreeNode

PYTHONIC:
- override of __init__ supporting ctor
- override of __iter__ supporting
- override of __len__ supporting
- override of __setitem__ supporting [] assignment syntax
- override of __getitem__ supporting [] access syntax
- override of __contains__ supporting 'in' syntax
- optional parameters with defaults for creating TreeNodes

"""

class BinarySearchTree:

    # external exception type
    INVALID_OP_FOR_EMPTY_MSG = "Cannot execute this operation on an Empty BST."
    KEY_NOT_FOUND_MSG = "Search Key Not Found"
    BST_INPUT_VALIDATION_MSG = "For BST validation:  Input BST, min, max values cannot be None."
    INSERTION_OF_DUPLICATE_KEY_MSG = "Cannot insert duplicate key.  BST for unique keys only."

    # NOTE:  tracks MAX RANGE of keys in BST;
    #        enforced on property TEST,
    #        can be done DURING or AFTER BULK INSERT!
    MIN_KEY = 0
    MAX_KEY = 100

    # NOTE:  root and size, where EMPTY tree is supported with root as NULL/None
    def __init__(self, min=0, max=100):
        self.root = None
        self.size = 0
        self.MIN_KEY = min
        self.MAX_KEY = max

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # NOTE:  support iterator on this BST parent class!
    def __iter__(self):
        return BSTiterator(self)


    # NOTE:  BREADTH-FIRST TRAVERSAL of tree to print contents
    #        Doing this traversal with LOOP instead of incurring exponential recursive time-complexity
    def printContents(self):
        print "[";
        bfsContents = []
        if (self.root is None):
            pass
        else:
            bfsOrder = [ self.root ]
            while (bfsOrder):
                currentNode = bfsOrder.pop(0)
                bfsContents.append(currentNode)
                if (currentNode.hasLeftChild()):
                    bfsOrder.append(currentNode.leftChild);
                if (currentNode.hasRightChild()):
                    bfsOrder.append(currentNode.rightChild);

            for walkBFS in bfsContents:
                print (walkBFS.key, walkBFS.value)

        print "]"

    def isBST(self, min, max):

        # validate for inputs
        if (not self or not min or not max):
            raise ValueError(self.BST_INPUT_VALIDATION_MSG)

        # CASE 0:  test for DEGENERATE cases:
        # - EMPTY tree
        # - OR tree with ONE node
        if ((not self.root) or ( self.size == 1 )):
            return True

        if (min > self.root.key):
            return False
        elif (max < self.root.key):
            return False
        else:
            # ATTENTION:  gradual range-narrowing within subtrees of successively lower root nodes, BUT based on PARENT-ROOT-KEY range partitioning!
            return (self.isBST(self.root.leftChild, self.MIN_KEY, self.root.key) and self.isBST(self.root.rightChild, self.root.key, self.MAX_KEY))


    # NOTE:  INTERNAL RECURSIVE implementation
    # - ALGO:  - if key is LESS than current node; go left, otherwise go right
    #          - if nowhere further to go; then create new node as left or right child
    #          - NO INSERT, ALWAYs a new child!
    #          - therefore BST structure is INPUT-DRIVEN!
    # - self is a BST Tree VS CURRENT TreeNode being compared
    # - recursive helper function with currentNode position
    # - does key comparisons to decide next navigation
    # - checks existence of child before creating a new TreeNode
    def __put__(self,key,value,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self.__put__(key,value,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,value,parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                   self.__put__(key,value,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,value,parent=currentNode)
        # NOTE:  BLOCKs DUPLICATE insertions!
        elif key == currentNode.key:
            raise ValueError(self.INSERTION_OF_DUPLICATE_KEY_MSG)

    # NOTE: EXTERNAL implementation,
    #       - takes care of degenerate case of an EMPTY BST where root is None
    #       - updates the SIZE
    def put(self,key,value):
        if self.root:
            self.__put__(key,value,self.root)
        else:
            self.root = TreeNode(key,value)
        self.size = self.size + 1;

    # NOTE:  supports set element [] syntax
    def __setitem__(self,k,v): self.put(k,v)

    # NOTE:  - recursive helper function with currentNode position
    #        - self is a BST Tree VS CURRENT TreeNode being compared against
    #        - returns NODE for reuse
    def __get__(self, searchKey, currentNode):
        # NOTE:  exit immediately on None case, before accessing further
        #        so SIMPLIFY having to check hasRightChild(), hasLeftChild() cases!
        if not currentNode:
            return None
         # searchKey matches; so return found node
        elif currentNode.key == searchKey:
            return currentNode
        # searchKey is smaller; so search LEFT
        elif searchKey < currentNode.key:
            return self.__get__(searchKey, currentNode.leftChild)
        # searchKey is bigger; so search RIGHT
        else:
            return self.__get__(searchKey, currentNode.rightChild)

    # NOTE: EXTERNAL implementation,
    #       - takes care of degenerate case of an EMPTY BST where root is None
    #       - returns VALUE itself, rather than internal Node structure!
    def get(self, searchKey):
        # NOTE:  exit immediately on degenerate empty tree case, before accessing further
        if not self.root:
            return None
        else:
            found = self.__get__(searchKey, self.root)
            if not found:
                return None
            else:
                return found.value

    # NOTE:  supports get element [] syntax, delegates to get() returning VALUE
    def __getitem__(self, searchKey):
        return self.get(searchKey)

    # NOTE:  supports contsins() syntax, delegates to get() returning TRUE/FALSE
    def __contains__(self, searchKey):
        if self.get(searchKey):
            return True
        else:
            return False


    # NOTE:  this is method of BST itself, having meaning for MULTIPLE nodes
    # find Min
    # - just the leftmost LEAF
    def findMin(self, currentNode):
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode

    def delete(self, targetKey):
        # NOTE:  CASES for Delete
        # - CASE 0:  Handle case for Key not Found
        # - CASE 1:  EMPTY tree
        #   - do nothing, OR throw exception that cannot delete from an empty tree
        # - CASE 2:  ONE-node tree
        #   - replace root with None
        # - CASE 3:  target Node to delete is a LEAF (Left or Right)
        #   - just remove the target leaf from parent
        # - CASE 4:  Node to delete has ONLY one child (Left or Right)
        #   - replace target's parent (Left or Right) child,
        #     with target's own single child (Left or Right)
        # - CASE 5:  Node to delete has BOTH Children
        #   - replace target with its SUCCESSOR, or the Node with the NEXT LARGEST
        #   - replace left child of AFTER SUCCESSOR (RIGHT CHILD of target) with the right subtree of SUCCESSOR
        #   - replace value of target node with SUCCESSOR value
        #   - prior target LEFT child and RIGHT child relationships REMAIN INTACT

        # CASE 1:  EMPTY Tree
        if not self.root:
            raise ValueError(self.INVALID_OP_FOR_EMPTY_MSG)

        # CASE 2:  ONE-NODE Tree,
        if (self.size == 1):
            if (self.root.key == targetKey):
                self.root = None
                self.size = 0
                return self
            else:
                raise ValueError(self.KEY_NOT_FOUND_MSG)

        # CASE 3:  FIND TARGET RECURSIVELY
        # SURGICALLY SPLICE OUT TARGET, AVOIDING RECURSIVE SEARCH PERFORMANCE HIT
        foundNode = self.__get__(targetKey, self.root)
        if (not foundNode):
            raise ValueError(self.KEY_NOT_FOUND_MSG)
        else:
            # NOTE:  self-modification, no return necessary!
            self.__spliceOutTarget__(foundNode)

    def __spliceOutTarget__(self, targetNode):

        # CASE 3:  targetNode is a LEAF
        if (targetNode.isLeaf()):
            if (targetNode.isLeftChild):
                targetNode.parent.leftChild = None
            else:
                targetNode.parent.rightChild = None
            self.size = self.size - 1
            return

        # CASE 4:  targetNode has only ONE child; so reconnect its parent to BYPASS the target to delete; and instead point to its child
        if  targetNode.isLeftChild():
            if (targetNode.hasLeftChild() and (not targetNode.hasRightChild())):
                targetNode.parent.leftChild = targetNode.leftChild
            elif (targetNode.hasRightChild() and (not targetNode.hasLeftChild())):
                targetNode.parent.leftChild = targetNode.rightChild
            self.size = self.size - 1
            return
        elif targetNode.isRightChild():
             if (targetNode.hasLeftChild() and (not targetNode.hasRightChild())):
                targetNode.parent.rightChild = targetNode.leftChild
             elif (targetNode.hasRightChild() and (not targetNode.hasLeftChild())):
                targetNode.parent.rightChild = targetNode.rightChild
             self.size = self.size - 1
             return

        # CASE 5:  targetNode has BOTH left and right children;
        #          - replace the target with its SUCCESSOR that will preserve the BST property
        #            or the MIN node in its RIGHT subtree!
        #          - RECONSTRUCT the tree to preserve BST property
        # **** CONFUSED:  see a BUG with Sedgewick's handling of this case!
        #             wherein http://algs4.cs.princeton.edu/32bst/BST.java.html
        #             the line:  x.right = deleteMin(t.right);
        #             seems to DROP the entire right subtree of original target node!
        #             BUG HERE is that you need an ADDITIONAL pointer to track SUCCESSOR, AND AFTER-SUCCESSOR, or PARENT of it
        #      => so INSTEAD of:
        #             Node t = x;
        #             x = min(t.right);
        #             x.right = deleteMin(t.right);
        #             x.left = t.left;
        #      => CHANGE to:
        #             Node matchedTargetNodeToDelete = x;
        #             Node successor = min(matchedTargetNodeToDelete.right);
        #             Node afterSuccessor = match
        # edTargetNodeToDelete.right;
        #             afterSuccessor.left = deleteMin(successor);
        #             // matchedTargetNodeToDelete.left and right can remain unchanged, as we've just patched up afterSuccessor with orphaned segment from relocating successor
        #             matchedTargetNodeToDelete.value = successor.value
        #
        #      THIS WORKS BECAUSE remainder of afterSuccessor left subtree is LESS than the afterSuccessor root key
        #      AND promotion of successor to be root of afterSuccessor is OK as it is LESS than afterSuccessor,
        #      AND greater than remainder left subtree of deleted target node
        followingSuccessor = targetNode.rightChild
        successor = self.findMin(followingSuccessor)
        # NOTE:  successor is assured to NOT have a left child
        orphanedFromDeleteSuccessor = successor.rightChild
        followingSuccessor.leftChild = orphanedFromDeleteSuccessor
        # in-place targetNode replacement with successor key and values
        # ATTENTION that leftChild and rightChild REMAIN intact
        targetNode.key = successor.key
        targetNode.value = successor.value
        self.size = self.size - 1
        return

        # NOTE:  self-modification, so no return necessary!



