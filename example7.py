class EvenLengthMixing:
    def even_length(self):
        return len(self) % 2 == 0
    
class MyList(list, EvenLengthMixing):
    pass

class MyDict(dict, EvenLengthMixing):
    pass

x = MyDict()
x["key"] = "value"
x["another key"] = "another value"
print(x.even_length()) # True