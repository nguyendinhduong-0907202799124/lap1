class Shop:
    def __init__(self,name,items):
        self.name=name
        self.items= items
    def get_items_count(self):
        print(len(self.items))
    
shop=Shop('My shop',['Apples','Bananas','Cucumbers'])
shop.get_items_count()
        

