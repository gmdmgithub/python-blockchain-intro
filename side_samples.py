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
    print('########### decompose ################')
    stats = [('name','greg'),('age',28),('tall',True)] #list of tuple
    dict_stats = { key:value for (key,value) in stats} # way to decompose tuple
    print(dict_stats)

decompose()

def comprehend():
    """ Sample comprehension with else statement """
    print('########### comprehend################')
    test_list = [3,5,6,9,10]
    print('comprehend: ',test_list)
    
    dupl_add = [ el for el in test_list if el%2 == 0]
    print('Print if element % 2 is zero',dupl_add)
    
    seed_list = [3,9]
    dupl_add = [ el for el in test_list if el in seed_list]
    print('Print element if the element is in seed list',dupl_add)

comprehend()

def for_enumerate():
    """ Test of the function whitch combain index and data
    thanks to enumerate - enumerate brings a tupe as a returned object """
    print('########### enumerate ################')

    value = {'id': 1,'age': 22, 'name':'greg'}
    value_list = [value]
    value = {'id': 2,'age': 30, 'name':'greg2'}
    value_list.append(value)
    value = {'id': 3,'age': 48, 'name':'greg3'}
    value_list.append(value)

    sum = 0
    for (index, value) in enumerate(value_list):
        if index == 0:
            continue
        sum = sum + value['age']
        print(value)

    print(f'total age = {sum}')

for_enumerate()

print('########### copy by value and reference ################')

def make_copy():
    
    sample_list =[1,2,3,4,5]
    sample_list_copy = sample_list
    sample_list[0]=6
    print(f'Sample list: {sample_list} and {sample_list_copy} by reference')
    sample_list_copy = sample_list[:]
    sample_list[0]=1
    print(f'Sample list: {sample_list} and {sample_list_copy} by value')
    #some dictionary
    sample_dict = [{'name':'Greg'},{'age':29}]
    copy_sample_dict = sample_dict
    sample_dict[0] = {'name':'Alex'}
    print(f'Sample dict: {sample_dict} and {copy_sample_dict} by reference')
    
    
    copy_sample_dict = sample_dict[:]
    #this below are equivalent - but first cause by value second is only shallow
    #sample[0] = {'name':'Greg'}
    sample_dict[0]['name'] = 'Greg'
    #shallo means that the range selectors copies list, and primitives value not complex inside
    print(f'Sample dict: {sample_dict} and {copy_sample_dict} by shallow value') 

    #very useful copying dictionary to a tupel
    dict_to_tupel = sample_dict[0].items()
    print(dict_to_tupel)

make_copy()

print('########### any and all ################')
def check_any_all():
    """ Any or all chcecks if any element in the list is true or all are true
        We can use iteration to check it easily"""
    
    sample_list = [2,4,5,10,3,40]

    chceck_list = [ element < 20 for element in sample_list]
    print(chceck_list)

    print(any(chceck_list), all(chceck_list))

check_any_all()