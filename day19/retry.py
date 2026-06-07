import functools

class NotExpectedResult(Exception):
    pass

def retry(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(n):
                try:
                    a = func(*args,**kwargs)
                    print("Successful")
                    return a
                except:
                    print(f"{i+1} attempt failed!")   
            print("All attempts failed!")
            raise NotExpectedResult
        return wrapper
    return decorator

decorator = retry(3)
attempts = 0
@decorator
def greet():
    global attempts
    attempts += 1
    if attempts == 3:
        print("Hello")
    else:
        raise NotExpectedResult

greet()
