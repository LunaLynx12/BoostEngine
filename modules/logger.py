import os
import inspect
import datetime

class Logger:
    def __init__(self, log_file="boostengine.log"):
        self.log_file = log_file

    def log(self, message, level="INFO"):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        caller_frame = inspect.stack()[1]
        file_name = os.path.basename(caller_frame.filename)
        line_number = caller_frame.lineno

        with open(self.log_file, "a") as file:
            file.write(f"[{current_time}] [{level}] [{file_name}:{line_number}] {message}\n")
        