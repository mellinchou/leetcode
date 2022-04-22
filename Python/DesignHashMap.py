class MyHashMap:

    def __init__(self):
        self.hashmap=[]

    def put(self, key: int, value: int) -> None:
        for i in range(0,len(self.hashmap),2):
            if self.hashmap[i]==key:
                self.hashmap[i+1]=value
                return
        self.hashmap.append(key)
        self.hashmap.append(value)
        

    def get(self, key: int) -> int:
        for i in range(0,len(self.hashmap),2):
            if self.hashmap[i]==key:
                return self.hashmap[i+1]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(0,len(self.hashmap),2):
            if self.hashmap[i]==key:
                del self.hashmap[i:i+2]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)