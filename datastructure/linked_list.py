from .list_node import ListNode

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        
    def traverse(self):
        node_values = []
        current_node = self.head
        while current_node.next is not None:
            node_values.append(current_node.value)
            current_node = current_node.next
        return node_values
    
    def odd_or_even(self):
        results = []
        current_node = self.head
        while current_node.next is not None:
             
            results.append()