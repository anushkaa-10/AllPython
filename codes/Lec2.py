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
    
    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        curr = self.head 
        while curr.next!=None:
            curr = curr.next

        curr.next = new_node
        self.n +=1

    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr!=None:
            if curr.data == after:
                break
            curr = curr.next

        if curr!=None:
            new_node.next = curr.next
            curr.next = new_node
            self.n +=1

        else:
            return 'not found'
        
    ##Deletion
    def clear(self):
        self.head = None
        self.n = 0
    
    def del_head(self):
        if self.head==None:
            return 'emptyyyy'
        self.head = self.head.next
        self.n -=1

    def pop(self):
        if self.head == None:
            return 'emptyyyyyList'
        curr = self.head
        if curr.next ==None:
            return self.del_head()
        while curr.next.next !=None:
            curr = curr.next
        curr.next = None
        self.n -=1

    def remove(self,value):
         
         if self.head == None:
             return 'Empty LL'
         
         if self.head.data == value:
             return self.del_head()
         
         curr = self.head

         while curr.next!=None:
             if curr.next.data == value:
                 break
             curr = curr.next

         if curr.next ==None:
             return 'not found'
         else:
             curr.next = curr.next.next

    #search
    def search(self,value): 
        curr = self.head
        pos = 0
        while curr!=None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'not found'
    
    def __getitem__(self,index):
        curr = self.head
        pos =1
        while curr!=None:
            if pos==index:
                return curr.data
            curr = curr.next
            pos +=1

    def replace_max(self,value):
        temp = self.head
        max = temp 

        while temp!=None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data=value

    def sum_odd(self):
        temp = self.head
        cnt =0

        while temp!=None:
            if cnt%2!=0:
                res += temp.data

            cnt+=1
            temp = temp.next

        print(res)

    def reverse(self):
        prev_node = None
        curr = self.head

        while curr!=None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head = prev_node

    
L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(5)
L.insert_after(3,9)
L.replace_max(3)
L.reverse()
print(L)