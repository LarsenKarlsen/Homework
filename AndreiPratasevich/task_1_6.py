def convert_tup_to_int(t):    
    return int(''.join([str(x) for x in t]))

def pretty_print(a,b,c,d):
    first_row = [str(i) for i in range(c,d+1)]
    gap = ' ' * 5

    print(gap + gap.join(first_row))

    for num in range(a,b+1):
        row = str(num)
        row += ' ' * (5-len(str(num)))
        for mul in first_row:
            row += f'{num * int(mul)}' + ' ' * (6-len(f'{num * int(mul)}'))
        print(row)
        


pretty_print(2,4,3,7)