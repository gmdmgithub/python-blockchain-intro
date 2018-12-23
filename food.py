class Food:
    def __init__(self,name, kind):
        self.name = name
        self.kind = kind
    
    @property
    def name(self):
        return self.__name[:]
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def kind(self):
        return self.__kind[:]
    @kind.setter
    def kind(self,value):
        self.__kind = value
    
    
    def describe(self):
        return f'My name: {self.name} and I am a kind of {self.kind}'

if __name__ == '__main__':
    my_food = Food('Roll','Bread')
    print(my_food.describe())
