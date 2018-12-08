import math

name = 'Greg'
age = 38

def print_me():
    """ Function to print name and age"""
    print(f"My name is {name} and I'm {age}")


def print_two_data(data1,data2):
    """ Function to print two data as one string
        Arguments:
        data1: any
        data2: any
    """
    print(f"Two data: {data1} and: {data2}")

def print_dacades_from_age():
    #print(f"You live: {math.floor(age/10)} dacads")
    print(f"You live: {(age//10)} dacads")

print_me()

print_two_data('test', 2.34)

print_dacades_from_age()

