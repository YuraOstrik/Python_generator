#First
a = 0
b = 10
def even_list(a,b):
    for i in range(a,b + 1):
        if i % 2 != 0:
            yield i



print(list(even_list(a,b)))

#Second

list_author = [2,3,11,5,6]

ret_list = lambda a,b: (list(filter(lambda x: x not in list_author, range(a,b+1))))

print(ret_list(0,10))

#Third

def show_line(symbol):
    def function_to_call(replay):
        if replay == 0:
            print(20 * symbol)
        else:
            for i in range(10):
                print(symbol)
    return function_to_call

f = show_line("#")
f(0)

#Fourth - Fifth
import time
def decorator(func):
    def wrapper(start):
        result = func()
        end = time.time()
        print(f"Time: {end - start} seconds")
        return result
    return wrapper

@decorator
def get_decorator():
    time.sleep(5)
    
start = time.time()
get_decorator(start)









