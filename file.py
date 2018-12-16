my_file = open('test.txt',mode='r+') # modes r = read, w - write, r+ - read and write, 
                          #x - clreate and write, a - append, write and append to the end, b - open in binarymode
#content = my_file.read()
# my_file.write('Hi there 1\n')
# my_file.write('Hi there 2\n')
# my_file.write('Hi there 4\n')

# content = my_file.readlines()

# print(content)

# for line in content:
#     print(line[:-1]) # prevent reading \n caracter


# read line by line

line = my_file.readline() 
while line:
    print(line)
    line = my_file.readline()

my_file.close()