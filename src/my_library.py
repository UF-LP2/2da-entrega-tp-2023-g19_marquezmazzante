from binarytree import Node as OriginalNode

class MyNode(OriginalNode):
    def __init__(self, value, name, left=None, right=None):
            super().__init__(value,left,right)
            self.name = name
