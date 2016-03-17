from BST.treenode import TreeNode

class BSTiterator:

    # initialize to associated binary search tree's root treenode
    def __init__(self, bst):
        self.nextNode = bst.root

        # TODO : CAN choose to capture a SNAPSHOT of data structure at time of iterator ctor!
        #       THEN iterate thru THAT with next()

        #       OTHERWISE using a GENERATOR for real-time generation UPON next() access, RISKS
        #       UNPREDICTABLE results on concurrent adding of elements which may be orphaned?
        #       THEREFORE, BST is inappropriate data structure for data to be changed after start of iteration?

        """
        self.capturedBST = bst.root
        for elem in self.capturedBST:
            self.snapshot.append((elem.key, elem.value))
        """

    # ONLY iterator can iterate on ITSELF; and the collection on which it iterates is ITERABLE with __iter__ override!
    def __iter__(self):
        return self

    # NOTE, returns FALSE when next value is None
    def hasNext(self):
        return (self.next())

    # @returns value within treenode that is the next in an INORDER tree traversal,
    #                which itself raises StopIteration error if None is reached
    def next(self):

        if (self.nextNode is None):
            raise StopIteration("UNABLE to iterate over empty tree.");
        else:
            # for syntax WILL invoke treenode __iter__ stateful yield method, but on NEWLY-INITIALIZED START state!
            # HOWEVER, FAILED attempt to BREAK loop to limit state update to just transition to NEXT node, thus PROPAGATING YIELD from baseline treenode!
            # MESSINESS:  TreeNode generator-based iterator MUST be invoked through for ... in syntax, and CANNOT be invoked explicitly like self.nextNode.__iter__() which returns Python GENERATOR
            # eg for elem in self.nextNode:
            # INSTEAD can have this next() method RETURN the element pair value to be accessed
            #         AND update self.nextNode to the NEXT iteration state!
            # self.nextNode = self.nextNode.__iter__()

            return (self.nextNode.key, self.nextNode.value)

        # NOTE:  treenode generator method in its __iter__ will raise StopIteration(..) exception if no next node exists

        # TODO:  ALTERNATIVE is to have this generator generate/yield the latest in ctor-captured collection SNAPSHOT!


