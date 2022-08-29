from .tree_node import TreeNode

class Tree:

    def __init__(self):
        self.root = None
        
    def depth_first_traversal_itter(self):
        if not self.root:
            return []
        values = []
        stack = [self.root]
        while(stack):
            current_node = stack.pop()
            values.append(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return values
    
    def depth_first_traversal_recursive(self):
        if not self.root:
            return []
        left_values = self.depth_first_traversal_recursive(self.root.left)
        right_values = self.depth_first_traversal_recursive(self.root.right)
    
    def breadth_first_traversal(self):
        pass

    def insert(self, data):
        pass