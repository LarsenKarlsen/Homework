test = ['red', 'white', 'black', 'red', 'green', 'black']
result = ['black', 'green', 'red', 'white',]

def uniq_words(words):
    uniq_list = list(set(words))
    uniq_list.sort()
    return uniq_list


# print(uniq_words(test))

# print(f'Are result and output of function equal ? ANSWER: {uniq_words(test)==result}')

def div_brut (num):
    divs = []
    for i in range(1,num+1):
        if num%i == 0:
            divs.append(i)
    return divs

print(div_brut(60))