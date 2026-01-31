from pathlib import Path
from decimal import Decimal, InvalidOperation

NAME_MAX_LENGTH = 20

# Validate a full text file, containing multiple preset strings

def validate_preset_file(preset_file: Path) -> bool:
    
    if not preset_file.exists():
        raise FileNotFoundError
    
    preset_list = preset_file.read_text().splitlines() # List of preset strings
    valid_list = [] # Corresponding valid lines indexes

    invalid_preset_count = 0
    valid_preset_count = 0

    for i,preset in enumerate(preset_list):

        if validate_preset(preset):
            valid_list.append(i) # Marks preset as valid
            valid_preset_count += 1

        else:
            invalid_preset_count += 1
    
    valid_preset_list = [preset_list[i] for i in valid_list] 

    valid_preset_output = "\n".join(valid_preset_list) + "\n" # Creates text of valid presets

    print(f"Valid Files: {valid_preset_count}\nInvalid Files: {invalid_preset_count}") 
    # reports output for maintenance purposes
    
    

# Validate a full preset string, given in the form "name,coeff,intercept..."

def validate_preset(preset_string: str, error_file: Path) -> bool: 
    
    preset_values_list = preset_string.split(",")

    if len(preset_values_list) != 9:
        write_error(preset_string,error_file)
        return False 
    
    # Run every validation on the corresponding value(s)
    validation_suite = [
        validate_coefficient(preset_values_list[1]),
        validate_intercept(preset_values_list[2]),
        validate_coefficient(preset_values_list[3]),
        validate_intercept(preset_values_list[4]),
        validate_scalar(preset_values_list[5]),
        validate_scalar(preset_values_list[6]),
        validate_scalar(preset_values_list[7]),
        validate_scalar(preset_values_list[8])
    ]

    if not all(validation_suite): # There is one or more failures in the suite
        write_error(preset_string,error_file)
        return False 

    return True
    

# Write a malformed line to the given error file path

def write_error(preset: str,error_file: Path) -> None:

    if not error_file.exists(): # For testing purposes
        raise FileNotFoundError
    
    with open(error_file,"a") as f: # Write the preset to the error file 
        f.write(preset + "\n")

# Validate a coefficient 

def validate_coefficient(coefficient: str) -> bool:

    try: 
        decimal_coefficient = Decimal(coefficient) # Attempts to convert string to decimal type

    except InvalidOperation:
        return False # In case the string is not numeric

    if decimal_coefficient <= Decimal("0"): # Checks for negative or zero values
        return False
    
    return True

# Validate an intercept

def validate_intercept(intercept: str) -> bool:
    
    try: 
        decimal_intercept = Decimal(intercept) # Tries to convert intercept to Decimal

    except InvalidOperation:
        return False 
    
    if decimal_intercept < Decimal("0"): # 0 values and above are accepted
        return False
    
    return True

# Validate a scalar value 

def validate_scalar(scalar: str) -> bool:

    try:
        decimal_scalar = Decimal(scalar)
    
    except InvalidOperation: # Checks for Decimal error
        return False
    
    if decimal_scalar <= Decimal("0"): # Scalars must be positive values
        return False
    
    return True

# Validate the length of the name

def validate_name(name: str) -> bool:

    if len(name) > NAME_MAX_LENGTH: # Uses global constant to validate name length
        return False
    
    return True 


