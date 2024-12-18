import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # c type array size = c.size
        self.A = self.__make_array(self.size)

    
    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return result[:-1] 
    
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else: return "NA"

    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n +1

    def pop(self):
        if self.n==0:
            return "empty"
        print(self.A[self.n-1])
        self.n = self.n-1

    def clear(self):
        self.n=0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'Value error'
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i]= self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def __delitem__(self,pos):
        if 0<=pos <self.n:
            for i in range(pos,self.n-1):
              self.A[i] = self.A[i+1]

            self.n = self.n -1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        
    def sort(self):
        for i in range(self.n-1):
            for j in range(self.n-i-1):
                if self.A[j]>self.A[j+1]:
                    self.A[j],self.A[j+1] = self.A[j+1],self.A[j]

    def min(self):
        if self.n==0:
            return 'empty'
        min_val = self.A[0]
        for i in range(1,self.n):
            if self.A[i]<min_val:
                min_val = self.A[i]
        return min_val
    
    def max(self):
        if self.n==0:
            return 'empty'
        max_val = self.A[0]
        for i in range(1,self.n):
            if self.A[i]>max_val:
                max_val = self.A[i]
        return max_val
    
    def sum(self):
        if self.n==0:
            return 0
        total =0
        for i in range(self.n):
            if not isinstance(self.A[i],(int,float)):
                raise TypeError(f"Non-numeric value found: {self.A[i]}")
            total += self.A[i]
        return total

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __make_array(self,capacity):
        return(capacity*ctypes.py_object)()

   

L = MeraList()
L.append(5)
L.append(1)
L.append(4)
L.append(3)
L.append(2)

print("List:", L)
print("Minimum value:", L.min())
print("Maximum value:", L.max())
print("Sum of elements:", L.sum())

L.sort()
print("List after sorting:", L)
print("Sum of elements (after sorting):", L.sum())