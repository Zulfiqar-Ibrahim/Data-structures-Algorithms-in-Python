class Node():
    
    def __init__(self,key):
        
        self.value =  key 
        
        self.left = None
        
        self.right = None
    
#n1 =  Node(12)

#print(n1.value)

class Tree:
    
    def __init__(self):
        
        self.root = None
        
    def get_root(self):
        
        return self.root
    
    def add(self,val):
        
        if self.root is None:
            
            self.root = Node(val)
                        
        else:
            
            self._add(val,self.root)
    
    def _add(self,val,node):
        
        
        if val < node.value :
            
            if node.left is not None :
                
                self._add(val,node.left)
                
            else:
                
                node.left = Node(val)
        else:
            
            if node.right is not None:
                
                self._add(val,node.right)
                
            else:
                node.right = Node(val)
                
    def find(self,value):
        
        if self.root is not None:
            
            return self._find(value, self.root)
        else:
            None
    def _find(self, val, node):
        
        if val == node.value:
            
            return node
        
        elif val < node.value and node.left is not None:
            
            return self._find(val,node.left)
              
        elif val > node.value and node.right is not None:
            
            return self._find(val,node.right)
    def delete_tree(self):
        
        self.root = None
        
    def printtree(self):
        
        if self.root is not None:
            
            return self._printtree(self.root)
    def _printtree(self, node):
        
        if node is not None:
            
            self._printtree(node.left)
            
            print(str(node.value) + " ")
            
            self._printtree(node.right)
            
            
tree = Tree()

tree.add(3)

tree.add(4)

tree.add(0)

tree.add(8)

tree.add(2)

tree.printtree()

print(tree.find(8).value)
            