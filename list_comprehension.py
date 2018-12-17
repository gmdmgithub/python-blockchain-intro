from functools import wraps
import random

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

float_value=20/3
print(f'Test of format{float_value:^10.3f}')


print('################### import FUNC task1 ############################')

import random

random.seed()

print(random.random())
print(random.randrange(1,10))
print(random.uniform(1,10))

print('################### import FUNC task2 ############################')

from datetime import datetime
 
year = random.randint(1950, 2000)
month = random.randint(1, 12)
day = random.randint(1, 28)
birth_date = datetime(year, month, day)
print(birth_date.isoformat(timespec='auto'))
print(birth_date.strftime("%Y %m %d"))

print('################### decorator!!!! - how it works ############################')
#usually it works with inner functiuon!

def mapper(func):
    
    @wraps(func)  #wraps from functools replace the doc from original function
    def inner_func(list_of_values):
        return [func(value) for value in list_of_values]
    
    return inner_func

@mapper
def camel_func(str):
    """ return camelised string from python way string """
    return ''.join([st.capitalize() for st in str.split('_')])

#camel_func = mapper(camel_func) #this is the same as mapper!


# print('camel_func res: '+camel_func('test_the_camel_func'))

teams = ['manchester_united', 'bayern_munchen','ajax_amsterdam']

print(camel_func(teams))
print(camel_func.__doc__)

print('################### decorator with arguments !!!! - how it works ############################')

#decorator

def power_func(power):

    def mapper(fnc):
        def iner():
            return fnc()**power      
        return iner
    return mapper


@power_func(2)
def random_odd_choice():
    return random.choice([1,3,5,7,9])

print('random choice '+ str(random_odd_choice()))