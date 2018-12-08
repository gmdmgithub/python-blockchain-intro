names = ['Adam', 'Leon','Maximilian','Alexandre','Greg']

for name in names:
    print(len(name))
    if(len(name)>5):
        print(f'Name: {name} is longer then 5 letters!')
    if(name.lower().find('n') >=0):
        print(f'Name: {name} has letter n!!')

while len(names) > 0:
    names.pop()

print(names)