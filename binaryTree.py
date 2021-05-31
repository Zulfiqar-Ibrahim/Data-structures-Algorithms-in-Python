class Node:

    def __init__(self,data):



        self.left=None
        self.right=None
        self.data=data


class Tree:

    def __init__(self):
        
        self.root=None

    def get_root (self, value):

        return self.root

    def add(self,value):
        """[This methos check whether the node is root or not and if not then call recurcive _add(value,node) to 
        add the node on either left or right.]

        Args:
            value ([number]): [value of node]
        """

        if self.root is None:

            self.root=Node(value)

        else:
            
            self._add(value,self.root)
        
    def _add(self,value, node):
        """[summary]

        Args:
            value ([value]): [value of node]
            node ([node]): [every node has two left and right and data value]
        """

        if value < node.data:

            if node.left is not None: 

                self._add (value,node.left)
            else:
                node.left=Node(value)
            
        else:
            if node.right is not None: 

                self._add(value,node.right)
            else:
                node.right=Node(value)
    def printTree(self):
        """[check if there is no None root and if there is no None 
        then call the recursive function _printTree()]"""

        if self.root is not None:

            self._printTree(self.root)

    def _printTree(self, node):
        """[Travers the node.left and print its data and then traverse to node.right]

        Args:
            node ([node]): [node.left,node.right,node.data]
        """

        if node is not None:

            self._printTree(node.left)

            print(str(node.data) + ' ')

            self._printTree(node.right)

tree=Tree()

tree.add(50)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.printTree()





