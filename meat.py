from food import Food

class Meat(Food):
    def __init__(self,name, kind):
        super().__init__(name,kind)
    def cook(self):
        print(f'Hi, here is {self.name} I am cooking')

beef = Meat('beef','meat')
print(beef.describe())
beef.cook()