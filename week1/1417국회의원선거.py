class MaxHeap:
    def __init__(self):
        self.__data = []

    def insert(self, item):
        self.__data.append(item)
        index = len(self.__data)-1

        while index>1:
            if self.__data[index] > self.__data[index//2]:
                self.__data[index], self.__data[index//2] = self.__data[index//2], self.__data[index]
                index = index//2
            else:
                break

        
    def delete(self):
        if len(self.__data)>1:
            self.__data[1], self.__data[-1] = self.__data[-1], self.__data[1]
            temp = self.__data.pop()
            self.myHeapify(1)
            return temp
        else:
            return -1

    
    def myHeapify(self, index):
        left = index*2
        right = index*2+1
        max_index = index

        if self.__data[max_index] < self.__data[left]:
            max_index = left
        if self.__data[max_index] < self.__data[right]:
            max_index = right
        
        if max_index != index:
            self.__data[max_index], self.__data[index] = self.__data[index], self.__data[max_index]
            self.myHeapify(max_index)
            
