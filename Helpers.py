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
    def set_variable(var_name, var_type, var_value):
        new_var = dict()
        new_var["var_name"] = var_name

        validated_type = Helpers.validate_type(var_value)

        if var_type == "any":
            new_var["var_type"] = validated_type
        else:
            if var_type != validated_type:
                verge_data.error = True
                return Errors.INVALID_VARIABLE_TYPE(var_type, validated_type)
            else:
                new_var["var_type"] = var_type
        
        # Evaluating the variable value
        if new_var["var_type"] == "string":
            new_var["var_value"] = str(var_value).strip('"') # Removing ""
            new_var["var_value"] = str(var_value).strip("'") # Removing ''
        else:
            # Calculate variables
            calculated_value_str = ""
            retrieved_var_name  = ""
            for char in var_value:
                if char.isdigit() or char in "+-*/%^<>=":
                    if retrieved_var_name != "":
                        calculated_value_str += str(Helpers.get_variable(retrieved_var_name))
                        retrieved_var_name = ""

                    calculated_value_str += char
                else:
                    retrieved_var_name += char
            
            solved_value = eval(calculated_value_str)
            new_var["var_value"] = solved_value

            # Re assigning types for expressions
            final_type = Helpers.validate_type(solved_value)
            new_var["var_type"] = final_type

        verge_data.variable_store.append(new_var)