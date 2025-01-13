import verge_data
from Errors import Errors

class Helpers:
    @staticmethod
    def get_variable(var_name):
        for var in verge_data.variable_store:
            var_type = var["var_type"]
            var_value = var["var_value"]
            if var["var_name"] == var_name:
                if var_type == "int":
                    return int(var_value)
                elif var_type == "float":
                    return float(var_value)
                elif var_type == "string":
                    return str(var_value)
                elif var_type == "boolean":
                    return bool(var_value)
                else:
                    pass

        verge_data.error = True
        return Errors.VARIABLE_NOT_FOUND(var_name)
    
    @staticmethod
    def validate_type(var_value):
        # Validating the variable type
        if (str(var_value).startswith('"') and str(var_value).endswith('"')) or (str(var_value).startswith("'") and str(var_value).endswith("'")):
            validated_type = "string"
        elif str(var_value).isdigit():
            validated_type = "int"
        elif str(var_value).replace('.', '', 1).isdigit():
            validated_type = "float"
        elif str(var_value) == "true" or str(var_value) == "false":
            validated_type = "boolean"
        else:
            validated_type = None
        
        return validated_type

    @staticmethod
    def evaluate_expr(expr:str):
        new_expr:str = ""

        if Helpers.validate_type(expr) == "string":
            return expr
        
        var:str = ""
        variable_found = False
        expr += "!"
        for char in expr:
            if not variable_found and (char.isdigit() or char in "+-*/%^()<>="):
                new_expr += char
            else:
                variable_found = True
                if char not in "+-*/%^()<>=!":
                    var += char
                else:

                    if var.isdigit():
                        new_expr += var
                    elif var.isalnum():
                        new_expr += str(Helpers.get_variable(var.strip()))
                    else:
                        pass

                    if char != "!":
                        new_expr += char
                    var = ""
                    variable_found = False
        
        new_expr = eval(str(new_expr))
        return new_expr

    @staticmethod
    def set_variable(var_name, var_type, var_value):
        for var in verge_data.variable_store:
            if var["var_name"] == var_name:
                verge_data.error = True
                Errors.VARIABLE_RE_INIT(var_name)
                return

        new_var = {
            "var_name": var_name,
            "var_type": var_type,
            "var_value": var_value
        }

        if var_type == "boolean":
            new_var["var_value"] = eval(var_value)
            verge_data.variable_store.append(new_var)
            return


        # Evaluating the variable value
        new_var["var_value"] = str(Helpers.evaluate_expr(var_value))

        if var_type == "any":
            new_var["var_type"] = str(Helpers.validate_type(str(new_var["var_value"])))
            # Adding the variable to the store
            verge_data.variable_store.append(new_var)
            return
        
        if var_type != Helpers.validate_type(str(new_var["var_value"])):
            verge_data.error = True
            Errors.INVALID_VARIABLE_TYPE(var_type, Helpers.validate_type(str(new_var["var_value"])))
            return

        verge_data.variable_store.append(new_var)
