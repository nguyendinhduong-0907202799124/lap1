class Store:
    def __init__(self,name,type,capacity):
        self.name=name
        self.type=type
        self.capacity=capacity
        self.items={}
    @classmethod
    def from_size(cls, name, store_type, size):
        capacity = size * 2
        return cls(name, store_type, capacity)
    def add_items(self):
        if self.size+1<=self.capacity:
            print(self.name,'added to the store')
        else :
            print('Not enough capacity in the store')
    def remove_items(self,item_name,amount):
        self.item_name=item_name
        self.amount=amount
        if item_name in self.items and self.item_name >= amount:
            self.item_name -= amount
            if self.item_name==0:
                print(self.amount,self.item_name,'removed from the store')
        else:
            print('Cannot remove',self.amount,self.item_name)
    def __repr__(self):
        print(self.name,'of type',self.type,'with capacity',self.capacity)

first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)
print(first_store.add_items("potato"))
print(second_store.add_items("jeans"))
print(first_store.remove_items("tomatoes", 1))
print(second_store.remove_items("jeans", 1))