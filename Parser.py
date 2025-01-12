from Lexer import Lexer
from Visuals import Visuals
import verge_data
from Helpers import Helpers

class Parser:
    def parse(input_line):
        keyword = input_line.split()[0]
        line = ' '.join(input_line.split()[1:])

        if keyword == "var":
            lexed = Lexer.lex_variable(line)
            var_name = lexed["var_name"]
            var_type = lexed["var_type"]
            var_value = lexed["var_value"]
            
            # Storing the 
            Helpers.set_variable(var_name, var_type, var_value)