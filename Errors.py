from rich.console import Console
import verge_data

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

    @staticmethod
    def INVALID_VARIABLE_NAME(var_name):
        console.log(f"[red]Invalid variable name (Line {verge_data.counter})[/red]\nThe variable [underline yellow]{var_name}[/underline yellow] does not follow the variable naming conventions.")

    @staticmethod
    def INVALID_VARIABLE_TYPE(var_type):
        console.log(f"[red]Invalid variable type (Line {verge_data.counter})[/red]\nThe datatype [underline yellow]{var_type}[/underline yellow] is not defined or under the verge types system.")
    
    @staticmethod
    def VARIABLE_NOT_FOUND(var_name):
        console.log(f"[red]Variable not found (Line {verge_data.counter})[/red]\nThe variable [underline yellow]{var_name}[/underline yellow] was not found in the program.")

    @staticmethod
    def INVALID_VARIABLE_TYPE(var_type, validated_type):
        console.log(f"[red]Invalid type assignment (Line {verge_data.counter})[/red]\nThe type [underline yellow]{validated_type}[/underline yellow] cannot be assigned to type [underline yellow]{var_type}[/underline yellow].")

    @staticmethod
    def VARIABLE_RE_INIT(var_name):
        console.log(f"[red]VARIABLE RE-INITIALIZED (Line {verge_data.counter})[/red]\nThe variable [underline yellow]{var_name}[/underline yellow] cannot be initialized more than once.")
    @staticmethod
    def KEYWORD_NOT_FOUND(keyword):
        console.log(f"[red]KEYWORD NOT FOUND (Line {verge_data.counter})[/red]\nThe keyword [underline yellow]{keyword}[/underline yellow] is not found.")