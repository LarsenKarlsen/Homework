import os

data_path = os.path.join(os.getcwd(),'data/students.csv')

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, 'r') as data:
        stud_data = {}
        data.readline()
        for line in data.readlines():
            stud = {}
            stud['age'] = int(line.split(',')[1])
            stud['avg'] = float(line.split(',')[2][:-1])
            name = line.split(',')[0]
            stud_data[name] = stud

    sorted_studs = dict(sorted(stud_data.items(), key = lambda x:x[1]['avg'], reverse=True))
    top_names = list(sorted_studs.keys())[:number_of_top_students]
    
    return top_names

print(get_top_performers(data_path))