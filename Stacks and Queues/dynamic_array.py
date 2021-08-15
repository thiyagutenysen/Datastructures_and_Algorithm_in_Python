class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.array = [0]*self.capacity

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if k >= 0 and k < self.n:
            return self.array[k]
        else:
            raise Exception("Index out of range")

    def print_array(self):
        print("(", self.array, "capacity =", self.capacity, "n =", self.n, ")")

    def append(self, data):
        if self.n < self.capacity:
            self.array[self.n] = data
            self.n += 1
        else:
            self.resize(2*self.capacity)
            self.append(data)

    def pop(self):
        if self.n == 0:
            raise Exception("Cannot pop in Empty array, Index out of range")
        else:
            self.array[self.n-1] = 0
            self.n -= 1
            if self.n == self.capacity/4:
                self.resize(self.capacity//2)

    def resize(self, size):
        new_array = [0]*size
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = size

    def insert_at(self, index, data):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        if index >= 0 and index < self.n:
            for i in range(self.n-1, index-1, -1):
                self.array[i+1] = self.array[i]
            self.array[index] = data
            self.n += 1
        else:
            raise Exception("Index error")

    def remove_at(self, index):
        if index >= 0 and index < self.n:
            for i in range(index, self.n):
                self.array[i] = self.array[i+1]
            self.array[self.n-1] = 0
            self.n -= 1
            if self.n == self.capacity/4:
                self.resize(self.capacity//2)
        else:
            raise Exception("Index error")


darray = DynamicArray()
darray.print_array()
for i in range(17):
    darray.append(i)
    darray.print_array()
print(len(darray))
print(darray[8])
for i in range(17):
    darray.pop()
    darray.print_array()
print("-----------------------------")
darray.append(1)
darray.append(2)
darray.print_array()
darray.insert_at(1, 3)
darray.print_array()
darray.remove_at(2)
darray.print_array()
darray.insert_at(0, 4)
darray.print_array()
darray.remove_at(0)
darray.print_array()
