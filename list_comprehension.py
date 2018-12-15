def convert(dict):
    """ Function converts dictionary and print one of its field list """
    names = [person['name'] for person in persons]
    print(names)

def check_age(dict, min_age):
    """ Function chcecks if dectionary field age for all elements is grater then min_age """
    return all([person['age'] > min_age for person in persons])

def unpack_dict(dict):
    for (index,dv) in enumerate(dict):
        print(f'dictionary array element: {index}')
        for (key,val) in dv.items():
            print(key, val)

# Task 1
persons = [{'name':'Mike', 'age':27, 'hobbies':['music','tennis']},
            {'name':'Shon', 'age':34, 'hobbies':['sci-fi','football']},
            {'name':'Kriss', 'age':19, 'hobbies':['music','football']},
            {'name':'Anna', 'age':21, 'hobbies':['books','hiking']}]


# Task 2
convert(persons)

# Task 3
print(check_age(persons,18)) #should be True
print(check_age(persons,20)) # should be False

# Task 4
copy_persons = persons[:]
copy_persons[0] = {'name':'Adam','age':27, 'hobbies':['music','tennis']}
print(f'Are the same? copy: {copy_persons[0]} original: {persons[0]}')
#better way
copy_person2 = [person.copy() for person in persons]
copy_person2[0]['name'] = 'Adam'
print(f'Are the same? copy: {copy_person2[0]} original: {persons[0]}')

# Task 5
unpack_dict(persons)


############## lamba and other #######################
print('################### LAMBDA FUNC task1 ############################')
#call inside function
def inside_func(name):
    return f'hi from inside function {name}'

def call_inside_func(some_func):
    print(some_func('Alex'))

my_call = call_inside_func
my_call(inside_func)

print('################### LAMBDA FUNC task2 ############################')

# call faunction with lambda expression
my_call(lambda nick: f'I\'m in lambda {nick}')

print('################### LAMBDA FUNC task3 ############################')
#passing  ulimited number of arguments

def call_inside_func2(some_func, *args):
    for arg in args:
        print(some_func(arg))

call_inside_func2(lambda name: f'Hi my nane is {name}', 'Ana', 'John','Kriss')