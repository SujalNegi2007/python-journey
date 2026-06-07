import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Total Time Taken: {end_time - start_time}")
    return wrapper
@timer
def greet():
    print("Hello")

greet()
