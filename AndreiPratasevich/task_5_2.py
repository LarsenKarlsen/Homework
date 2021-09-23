import os

data_path = os.path.join(os.getcwd(), 'data/lorem_ipsum.txt')

def most_common_words(file_path):

    with open(file_path,'r') as df:
        text_data = df.read()

    text = text_data.split()

    words_count = {}

    for item in text:
        words_count[item.lower()] = words_count.get(item.lower(),0) + 1

    freq_d = dict(sorted(words_count.items(), key=lambda x:x[1], reverse=True))

    out = list(freq_d.keys())[:3]


    print(out)

most_common_words(data_path)