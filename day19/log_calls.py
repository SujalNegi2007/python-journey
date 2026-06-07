import time
import functools
from datetime import datetime
import logging
logging.basicConfig(
    level = logging.INFO,
    filename = "Log_file.txt",
    format = "%(asctime)s - %(message)s"
)

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        a = func(*args,**kwargs)
        end_time = time.time()
        logging.info(f"Function Name that was called: [{func.__name__}]\n"
                f"Arguments Were: [{args}, {kwargs}]\n"
                f"The value it returned: [{a}]\n"
                f"The Total time taken for the function to execute: [{end_time - start_time}]\n\n")
    return wrapper

@log_calls
def greet():
    return "Hello"

greet()
