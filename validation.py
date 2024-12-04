def validate_input(input_value, value_type):
    if value_type == "int":
        try:
            return int(input_value)
        except ValueError:
            print("Invalid input, please enter an integer.")
            return None
        
    elif value_type == "float":
        try:
            return float(input_value)
        except ValueError:
            print("Invalid Input, please enter a valid price.")
            return None
    return input_value
