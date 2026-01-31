from pathlib import Path

# Contains all the file management functions for the simulation program. 

# Given a text file path, loads it and returns the lines in a list

base = Path(__file__).parent
preset_dir = base / "presets"
text_file = preset_dir / "a.txt"

def load_file(path):

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.") # Checks if the path actually exists

    text = path.read_text()

    if text.strip() == "":
        raise FileNotFoundError(f"{path} is completely empty.")

    text_list = text.splitlines()

    return text_list

# Given a list of lines, find the line which represents the search term

def search_for_line(preset_list, target):

    if not preset_list:
        raise FileNotFoundError("File is empty.")

    for line in preset_list:

        preset = line.split(",")

        output_list = [preset[0]]
        output_list.extend(list(map(int, preset[1:]))) # Turns all numbers into int type
        
        if output_list[0] == target: # Target found
            return output_list 
        
    raise KeyError(f"Preset not in file list")

text_list = ["single"]

print(search_for_line(text_list,"single"))

