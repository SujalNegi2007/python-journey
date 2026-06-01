import time
from datetime import datetime
from grade_manager import log_file
def database(message):
    with open(log_file,"a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}], {message}\n")

class timer():
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self,*args):
        elapsed = time.time() - self.start
        database(f"The Code Took {elapsed:.3f} Seconds To Run.")

class InvalidMarksError(Exception):
    pass
