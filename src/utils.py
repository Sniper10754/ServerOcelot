import sys
from time import perf_counter
import typing

def merge_dict(x, y):
    return {**x, **y}

#* Setupper function
def time(return_func):
    
    #* Actual decorator
    def wtime(f):
        #* Inner func
        def inner(*args, **kwargs):
            start = perf_counter()
            r = f(*args, **kwargs)
            finish = perf_counter()
            
            return_func(start, finish)
            return r
        return inner
    
    #* Return the configured decorator
    return wtime

def prompt(*, prompt: str, options: typing.List[str] = ["y", "n"]):
    opts = ""
    
    for opt in options:
        opts = opts + f"{opt} "
    
    while True:
        choice = input(f"{prompt}, {opts}")        

        if choice in options: return choice
        else:                 return