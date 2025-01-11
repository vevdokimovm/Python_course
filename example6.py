class EvenLengthMixing:
    def even_length(self):
        return len(self) % 2 == 0
    
class MyList(list, EvenLengthMixing):
    pass

print(MyList.mro())
# [<class '__main__.MyList'>, <class 'list'>,
#  <class '__main__.EvenLengthMixing'>, <class 'object'>]
x = MyList([1, 2, 3])
print(x.even_length()) # False
x.append(4)
print(x.even_length()) # True