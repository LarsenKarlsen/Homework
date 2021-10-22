'''
Module provide decorators for RssParser.py.
Decorators used to print verbose messages.

All decorators checked if verbose flag is TRUE
If so print verbose msges
else return function
'''
from time import time
from datetime import datetime  

def time_converter(str_time):
    date = datetime.fromisoformat(str_time[:-1])

    return date.strftime('%Y%m%d')

def exec_time(func):
    '''   This function shows the execution time of 
    the function object passed'''
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        
        if args[0].verbose:
            print(f'Rss feed fetched and parsed in {(t2-t1):.4f}s')
    
        return result

    return wrap_func


def get_rss_log(f):
    '''
    Connection log decorator
    '''
    
    def wrapper(*args):

        if args[0].verbose:
            print('You see this messages becose you enable --verbose')
            print(f'Сonnecting: {args[1]}')
            print(f'Execute {f.__name__} ')
        return f(*args)
    
    return wrapper

def parse_log(f):
    '''
    Parser log decorator
    '''
    def wrapper(*args):

        if args[0].verbose:
            print(f'Start parsing RSS content')
            print(f'Execute {f.__name__} ')
            print(f'Parsing complete')
        return f(*args)
    
    return wrapper

def feed_log(f):
    '''
    Feed log decorator
    '''
    def wrapper(*args):
        if args[0].verbose:
            print(f'Execute {f.__name__}')
            print(f'In feed {len(args[0].feed)} items')
            print('Feed is rdy, enjoy!')
            print('Printing feed')
        return f(*args)
    return wrapper