class MoneyBox():
    coins_in = 0
    
    def __init__(self, capacity):
        self.capacity = capacity
        
    def can_add(self, v):
        if self.coins_in + v <= self.capacity:
            return True
        else:
            return False
        
    def add(self, v):
        self.coins_in += v
        
        
# x = MoneyBox(12)
# x.add(4)
# x.add(7)
# print(x.coins_in)

# if x.can_add(1):
#     x.add(1)
#     print("added 1")
#     print(x.capacity)
    
# if x.can_add(5):
#     x.add(5)
    
    
        