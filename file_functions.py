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

def search_for_line(text_list, target):

    for line in text_list:
        if (x := line.split(","))[0] == target:
            return x
    
    raise FileNotFoundError(f"Preset not in file list")

text_list = ["F15,324,325,364,342,3264","F16,32,23523,34635,235325,23"]

print(search_for_line(text_list,"F15"))

