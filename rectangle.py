#custom classes in python
#Description: You are tasked with creating a Rectangle class with the following requirements:
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width= width

    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}    

r = Rectangle(10,5)

for item in r:
    print(item)

