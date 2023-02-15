import csv

def read_file(filename):
    with open(filename,'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
                line = tuple(line.split(','))
                data.append(line)
    print('1',data)
    return columns,data
    
def write_to_base(filename):
    with open(filename,'w') as file:
        file.write(','.join(columns))
        for line in data:

            file.write(','.join(line))
            print(line)

def get_line():
    newline = tuple((input('enter data ')+'\n').split(' '))
    data.append(newline)
  
columns,data = read_file('db_1.csv')
get_line()
write_to_base('db_1.csv')

















