from food import Food
FRUIT_KIND = 'Fruit'
class Fruit(Food):
    def __init__(self,name):
        super().__init__(name,FRUIT_KIND)
    def clean(self):
        print(f'I am cleaning my name is {self.name} of {self.kind}')


apple = Fruit('apple')
apple.clean()