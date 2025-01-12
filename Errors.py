from rich.console import Console

console = Console()

class Errors:
    @staticmethod
    def error(title,message):
        console.log(f"[red]{title}[/red]\n{message}")

    @staticmethod
    def warning(title,message):
        console.log(f"[red]{title}[/red]\n{message}")

    @staticmethod
    def FNF(path):
        console.log(f"[red]File not found[/red]\nThe file [underline yellow]{path}[/underline yellow] is not found.\nCheck if the given path is the correct one.")

    @staticmethod
    def INVALID_FILE_TYPE(path):
        console.log(f"[red]File is not valid[/red]\nThe file [underline yellow]{path}[/underline yellow] is not a valid file type.")