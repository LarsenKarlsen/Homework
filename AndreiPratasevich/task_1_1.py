def string_len(string):
    len = 0
    if string == '':
        return len
    else:
        for word in string: # можно и через enumerate
            len+=1
    return len

s1='hello world'
s2='\n'
s3=''

test_cases = [s1,s2,s3,]

for test in test_cases:
    print(f'test case: {test}')
    print(f'python len = {len(test)} : my len = {string_len(test)} \n')