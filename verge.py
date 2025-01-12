import typer
import os
import time

from Visuals import Visuals
from Errors import Errors

# Typer instance
verge = typer.Typer()

@verge.command()
def run(path:str):
    start_time = time.time()
    if not os.path.exists(path):
        Errors.FNF(path)
        return
    
    if not path.endswith(".verge"):
        Errors.INVALID_FILE_TYPE(path)
        return
    
    Visuals.print(f"Running {path}...")
    end_time = time.time()

    Visuals.timestamps(start_time, end_time)



if __name__ == "__main__":
    verge()
