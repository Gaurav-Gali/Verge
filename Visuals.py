from rich.console import Console
from datetime import datetime

# Console instance
console = Console()

class Visuals:
    @staticmethod
    def print(text):
        console.print(f"{text}")

    @staticmethod
    def timestamps(start_time, end_time, accuracy=5):
        exec_time = end_time - start_time
        console.print(f"\n[dim]Executed in [green]{exec_time:.{accuracy}f}[/green] seconds[/dim]")


    