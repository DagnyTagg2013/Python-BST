import sys
import traceback
from BST.bst import BinarySearchTree

def main(args):

    # CASE 0:  CTOR on EMPTY tree
    print 'Hello2!'
    emptyTree = BinarySearchTree()
    print 'Hello3!'

    # CASE 1:  Breadth-First Traversal of EMPTY Tree;
    emptyTree.printContents()

    # CASE 2:  ONE-ITEM Tree
    oneTree = BinarySearchTree()
    oneTree.put(1, "ALPHA")
    oneTree.printContents()

    # CASE 3: TWO-ITEM Tree, with [] set syntax
    twoTree = oneTree
    twoTree[2] = "BETA"
    twoTree.printContents()

    # CASE 4: TEST for correct build of SIX-ELEMENT TREE
    # input:  5, 30, 2, 40, 25, 4
    # BFS Order:
    sixTree = BinarySearchTree()
    # sixTree:  5, 2, 30, 4. 25, 40
    sixTree.put(5, "FIVE")
    sixTree.put(30, "THIRTY")
    sixTree.put(2, "TWO")
    sixTree.put(40, "FORTY")
    sixTree.put(25, "TWENTY-FIVE")
    sixTree.put(4, "FOUR")
    sixTree.printContents()

    # CASE 5: FIND an element in an EMPTY tree
    # missing = emptyTree.get(5)
    # print("Value found in Empty Tree {0}".format(missing))

    # CASE 6:  FIND an element in a twoTree
    valueOne = twoTree.get(1)
    print valueOne
    print("'ONE' value found in Two Tree is:  {0}".format(valueOne))

    # CASE 7:  FIND an element in a sixTree, using [] syntax
    valueFive = sixTree[5]
    print("'FIVE' value found in Six Tree is:  {0}".format(valueFive))

    # CASE 8:  FIND set containment in a sixTree, using contains syntax
    doesContain = 25 in sixTree
    print("Does Six Tree contain 25:  {0}".format(doesContain))

    # CASE 9:  tricky deletion case where target node (3) to delete has TWO children
    """

         1
        / \
       0   3
          / \
         2   8
            / \
           5   9
            \
             6
              \
               7
    """
    trickyDeleteTree1 = BinarySearchTree()
    trickyDeleteTree1.put(1, "ONE")
    trickyDeleteTree1.put(3, "THREE")
    trickyDeleteTree1.put(8, "EIGHT")
    trickyDeleteTree1.put(9, "NINE")
    trickyDeleteTree1.put(0, "ZERO")
    trickyDeleteTree1.put(2, "TWO")
    trickyDeleteTree1.put(5, "FIVE")
    trickyDeleteTree1.put(6, "SIX")
    trickyDeleteTree1.put(7, "SEVEN")

    print("\nDELETE CASE1 for TrickyDeleteTree:  TARGET to delete has TWO CHILDREN\n")
    trickyDeleteTree1.printContents()
    trickyDeleteTree1.delete(3)
    print("TrickyDeleteTree1 AFTER deletion of key 3 is:")
    trickyDeleteTree1.printContents()

    # CASE 10: moderate deletion case where target node (5) to delete has ONE child
    """

         1
        / \
       0   3
          / \
         2   8
            / \
           5   9
            \
             6
              \
               7
    """
    trickyDeleteTree2 = BinarySearchTree()
    trickyDeleteTree2.put(1, "ONE")
    trickyDeleteTree2.put(3, "THREE")
    trickyDeleteTree2.put(8, "EIGHT")
    trickyDeleteTree2.put(9, "NINE")
    trickyDeleteTree2.put(0, "ZERO")
    trickyDeleteTree2.put(2, "TWO")
    trickyDeleteTree2.put(5, "FIVE")
    trickyDeleteTree2.put(6, "SIX")
    trickyDeleteTree2.put(7, "SEVEN")

    print("\nDELETE CASE2 for TrickyDeleteTree:  TARGET to delete has ONE CHILD\n")
    trickyDeleteTree2.printContents()
    trickyDeleteTree2.delete(5)
    print("TrickyDeleteTree2 AFTER deletion of key 5 is:")
    trickyDeleteTree2.printContents()

    # CASE 11: moderate deletion case where target node (2) to delete is a LEAF
    """

         1
        / \
       0   3
          / \
         2   8
            / \
           5   9
            \
             6
              \
               7
    """
    trickyDeleteTree3 = BinarySearchTree()
    trickyDeleteTree3.put(1, "ONE")
    trickyDeleteTree3.put(3, "THREE")
    trickyDeleteTree3.put(8, "EIGHT")
    trickyDeleteTree3.put(9, "NINE")
    trickyDeleteTree3.put(0, "ZERO")
    trickyDeleteTree3.put(2, "TWO")
    trickyDeleteTree3.put(5, "FIVE")
    trickyDeleteTree3.put(6, "SIX")
    trickyDeleteTree3.put(7, "SEVEN")

    print("\nDELETE CASE3 for TrickyDeleteTree:  TARGET to delete is a LEAF\n")
    trickyDeleteTree3.printContents()
    trickyDeleteTree3.delete(2)
    print("TrickyDeleteTree3 AFTER deletion of key 2 is:")
    trickyDeleteTree3.printContents()


    # CASE 12:  tricky deletion case where key to delete cannot be found
    trickyDeleteTree4 = BinarySearchTree()
    trickyDeleteTree4.put(1, "ONE")
    trickyDeleteTree4.put(3, "THREE")
    trickyDeleteTree4.put(8, "EIGHT")
    trickyDeleteTree4.put(9, "NINE")
    trickyDeleteTree4.put(0, "ZERO")
    trickyDeleteTree4.put(2, "TWO")
    trickyDeleteTree4.put(5, "FIVE")
    trickyDeleteTree4.put(6, "SIX")
    trickyDeleteTree4.put(7, "SEVEN")

    print("\nDELETE CASE4 for TrickyDeleteTree:  TARGET to delete cannot be found\n")
    trickyDeleteTree4.printContents()
    try:
        trickyDeleteTree4.delete(4)
    except ValueError as e:
        print(e.message)
    finally:
        print("TrickyDeleteTree4 AFTER deletion of key 4 is:")
        trickyDeleteTree4.printContents()

    # CASE 13:  degenerate deletion case where node to delete is the ONLY node in tree
    deleteTree5 = BinarySearchTree()
    deleteTree5.put(5,"FIVE")
    print("\nDELETE CASE5 for TrickyDeleteTree:  TARGET to delete is the ONLY node in tree\n")
    deleteTree5.printContents()
    print("DeleteTree5 AFTER deletion of key 5 is:")
    deleteTree5.delete(5)
    deleteTree5.printContents()

    # CASE 14: degenerate deletion case where tree is EMPTY
    deleteTree6 = BinarySearchTree()
    print("\nDELETE CASE6 for DeleteTree6: Tree is EMPTY\n")
    deleteTree6.printContents()
    try:
        deleteTree6.delete(4)
    except ValueError as e:
        print(e.message)
    finally:
        print("DeleteTree6 AFTER attempted deletion of key 4 is:")
        deleteTree6.printContents()


    # CASE 15: ITERATION of 3-node tree
    iterTree1 = BinarySearchTree()
    print("\nITERATION CASE1 for balanced 3-node tree\n")
    iterTree1.put(2,"TWO")
    iterTree1.put(1,"ONE")
    iterTree1.put(3,"THREE")
    iterTree1.printContents()
    print("\n START ITERATION:  \n")
    try:
        for elem in iterTree1:
            print ("KEY:  {0}; VALUE:  {1}\n".format(elem[0], elem[1]))
    except Exception as e:
        print (traceback.format_exc())


    # CASE 16:  ITERATION on 1-node tree
    # TODO:  ITERATOR IS NOT WORKING!!!


    # case 17:  ITERATION on empty tree
    """
    iterTree3 = BinarySearchTree()
    print("\nDELETE CASE3 for iterTree3: Tree is EMPTY\n")
    iterTree3.printContents()
    print("\n START ITERATION:  \n")
    try:
        for elem in iterTree3:
            print ("KEY:  {0}; VALUE:  {1}\n".format(elem.key, elem.value))
    except ValueError as e:
        print e.message
    """


# ATTENTION:  main entrypoint, for Python to emulate Java main entrypoint
if __name__ == '__main__':
    main(sys.argv)

