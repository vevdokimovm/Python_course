class ExtendedStack(list):
    def two_elem(self):
        return [self.pop(), self.pop()]
    
    def sum(self):
        a, b = self.two_elem()
        self.append(a + b)
        
    def sub(self):
        a, b = self.two_elem()
        self.append(a - b)
        
    def mul(self):
        a, b = self.two_elem()
        self.append(a * b)
        
    def div(self):
        a, b = self.two_elem()
        self.append(a // b)
        
st = ExtendedStack([1, 2, 3, 4, 5])
print(st)
st.sum()
print(st)
st.sub()
print(st)
st.mul()
print(st)
st.div()
print(st)