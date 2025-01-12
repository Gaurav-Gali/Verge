import typer
import os
import time

from Visuals import Visuals
from Errors import Errors
from Parser import Parser
import verge_data

# Typer instance
verge = typer.Typer()

@verge.command()
def run(path:str):
    start_time = time.time()
    # Main code starts
    if not os.path.exists(path):
        Errors.FNF(path)
        return
    
    if not path.endswith(".verge"):
        Errors.INVALID_FILE_TYPE(path)
        return
    
    # Reading the file
    with open(path, "r") as verge_file:
        verge_code = list()
        # Extracting each line of the code
        for line in verge_file:
            verge_code.append(line.strip())

        # Interpreting the code
        for line in verge_code:
            parse_res = Parser.parse(line)
            
            # Check for errors
            if verge_data.error:
                break
            
            Visuals.print(f"Variable store\n{verge_data.variable_store}")
            # Incrementing the program counter
            verge_data.increment_counter()


    # Main code ends
    end_time = time.time()
    Visuals.timestamps(start_time, end_time)



if __name__ == "__main__":
    verge()
