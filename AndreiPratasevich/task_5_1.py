import os

data_path = os.path.join(os.getcwd(), 'data/unsorted_names.txt')
out_data_path = os.path.join(os.getcwd(), 'task_5_1.txt')

names = []

with open(data_path) as df:
    for line in df:
        names.append(line)

names.sort()

with open(out_data_path, 'a') as fp:
    for name in names:
        fp.write(name)

print('Jobs done')