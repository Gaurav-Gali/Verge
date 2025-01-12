from enum import Enum
import verge_data
from Errors import Errors

# Types
Types = ["int", "float" , "string" , "boolean" , "any"]

class Lexer:
    @staticmethod
    def lex_variable(line):
        lexed_variable = {
            "var_name" : "",
            "var_type" : "",
            "var_value" : ""
        }

        # var age:int=10
        index = 0
        
        # Extracting the variable name
        while line[index] != ":":
            lexed_variable["var_name"] += line[index]
            index += 1
        index += 1
        lexed_variable["var_name"] = lexed_variable["var_name"].strip()
        # Check errors
        if lexed_variable["var_name"][0] in "1234567890!@#$%^&*()+-=[]{}|;':,.<>?/" + '"':
            verge_data.error = True
            Errors.INVALID_VARIABLE_NAME(lexed_variable["var_name"])

        # Extracting the variable type
        while line[index] != "=":
            lexed_variable["var_type"] += line[index]
            index += 1
        index += 1
        lexed_variable["var_type"] = lexed_variable["var_type"].strip()
        # Check errors
        if lexed_variable["var_type"] not in Types:
            verge_data.error = True
            Errors.INVALID_VARIABLE_TYPE(lexed_variable["var_type"])

        # Extracting the variable value
        lexed_variable["var_value"] = line[index:]
        lexed_variable["var_value"] = lexed_variable["var_value"].strip()


        return lexed_variable
        