import math

name = 'Greg'
age = 38

def print_me():
    """ Function to print name and age"""
    print(f"My name is {name} and I'm {age}")

print_me()

def print_two_data(data1,data2):
    """ Function to print two data as one string
        Arguments:
        data1: any
        data2: any
    """
    print(f"Two data: {data1} and: {data2}")

print_two_data('test', 2.34)

def print_dacades_from_age():
    #print(f"You live: {math.floor(age/10)} dacads")
    print(f"You live: {(age//10)} dacads")


print_dacades_from_age()

def decompose():
    """ Test decompose of dictionary from tuple """
    stats = [('name','greg'),('age',28),('tall',True)] #list of tuple
    dict_stats = { key:value for (key,value) in stats} # way to decompose tuple
    print(dict_stats)

decompose()

def comprehend():
    """ Sample comprehension with else statement """
    test_list = [3,5,6,9,10]
    dupl_add = [ el for el in test_list if el%2 == 0]
    print(dupl_add)
    seed_list = [3,9]
    dupl_add = [ el for el in test_list if el in seed_list]
    print(dupl_add)

comprehend()

def for_enumerate():
    """ Test of the function whitch combain index and data
    thanks to enumerate"""
    
    value = {'index': 0,'age': 2, 'name':'greg'}
    value_list = [value]
    value = {'index': 1,'age': 3, 'name':'greg2'}
    value_list.append(value)
    value = {'index': 2,'age': 4, 'name':'greg3'}
    value_list.append(value)

    sum = 0
    for (index, value) in enumerate(value_list):
        if index == 0:
            continue
        sum = sum + value['age']
        print(value)

    print(f'total age = {sum}')

for_enumerate()
    