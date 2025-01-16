import sys

def error_message_detail(error , error_detail:sys):
    
    _,_,exc_tb = error_detail.exc_info() # error details
    file_name = exc_tb.tb_frame.f_code.co_filename # file name
    
    error_message = f"Error Occured; Script Name: [{file_name}], Line Number [{exc_tb.tb_lineno}], Error Message[{str(error)}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys): 
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_detail = error_detail)
    
    def __str__(self):
        return self.error_message