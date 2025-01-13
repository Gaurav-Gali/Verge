from Lexer import Lexer
from Visuals import Visuals
import verge_data
from Helpers import Helpers
from Errors import Errors

keywords = [
    "var"
]

class Parser:
    def parse(input_line):
        if input_line == "":
            return
        if input_line.startswith("//"):
            return
        
        keyword = input_line.split()[0]
        line = ' '.join(input_line.split()[1:])

        if keyword not in keywords:
            verge_data.error = True
            Errors.KEYWORD_NOT_FOUND(keyword)
            return

        if keyword == "var":
            lexed = Lexer.lex_variable(line)
            var_name = lexed["var_name"]
            var_type = lexed["var_type"]
            var_value = lexed["var_value"]
            
            # Storing the 
            Helpers.set_variable(var_name, var_type, var_value)