import sys
from src.logger import logging

def error_message_detail(error, error_detail):
    _,_,exc_tb =sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name: {filename} at line number: {exc_tb.tb_lineno} with error message: {str(error)}"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message