from pathlib import Path

# Contains all the file management functions for the simulation program. 

# Given a text file path, loads it and returns the lines in a list

base = Path(__file__).parent
preset_dir = base / "presets"
text_file = preset_dir / "a.txt"

def load_file(path):

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.") # Checks if the path actually exists
    
    text = path.read_text().splitlines() # Provides a list containing the file's lines

    return text

print(load_file(text_file))
