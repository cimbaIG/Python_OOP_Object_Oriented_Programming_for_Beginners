from node import Node

# node_1 -> node_2 - node 1 points to node 2
# node_2 = Node(3)
# node_1 = Node(5, node_2)

# print(node_1.next is node_2)

# Define Nodes
 
# node_d = Node("d") 
# node_c = Node("c", node_d)
# node_b = Node("b", node_c)
# node_a = Node("a", node_b)
 
# # Print Attributes
 
# print("== Printing the Attributes ==")
 
# print(node_a.value) # node_a
# print(node_a.next)
 
# print(node_b.value) # node_b
# print(node_b.next)
 
# print(node_c.value) # node_c
# print(node_c.next)
 
# print(node_d.value) # node_d
# print(node_d.next)
 
# # Sequence
 
# print("=== Final Sequence ==")
 
# print(node_a.value)
# print(node_a.next.value)
# print(node_a.next.next.value)
# print(node_a.next.next.next.value)

from linked_list import LinkedList


my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)

print(my_linked_list.head.value)