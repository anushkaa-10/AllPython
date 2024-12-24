class Node:
    def __init__(self, value):
       self.data = value
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n +=1 

    def __str__(self):
        curr = self.head
        result = ''
        while curr!=None:
             result += str(curr.data) + '->'
             curr = curr.next
        
        return result+'None'

    
L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(L)