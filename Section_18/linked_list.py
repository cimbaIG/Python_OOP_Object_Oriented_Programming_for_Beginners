from node import Node


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_node(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next
            
            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
                
            new_node.next = runner
            previous.next = new_node
            
    def print_list_items(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print()

    # Wrapper function
    def print_reversed(self):
        self.print_reversed_recursive(self.head)
            
    # Recursive print method
    def print_reversed_recursive(self, node):
        if node is not None:
            self.print_reversed_recursive(node.next)
            print(node.value, end=" ")

    # Iterative implementation
    # def count_nodes(self):
    #     count = 0
    #     runner = self.head
        
    #     while runner is not None:
    #         count += 1
    #         runner = runner.next
        
    #     return count
    
    # Define a wrapper function
    def count_nodes(self):
        return self.count_nodes_recursive(self.head)
    
    # Recursive implementation
    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next)
    
    def find_node(self, target_value):
        runner = self.head
        
        while runner is not None:
            if runner.value == target_value:
                return True
            runner = runner.next
        
        return False
    
    def delete_node(self, target_value):
        if self.head is None:
            return False
        elif self.head.value == target_value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next
            
            while (runner is not None) and (target_value > runner.value):
                previous = runner
                runner = runner.next
                
            if (runner is not None) and (runner.value == target_value):
                # Bridge that skips the node we want to delete - previous node 
                # will now point to the node that comes right after the runner 
                # node.
                previous.next = runner.next
                return True
            else:
                return False