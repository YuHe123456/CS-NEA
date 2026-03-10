from pathlib import Path
from decimal import Decimal

# Contains all the file management functions for the simulation program. 

# Given a text file path, loads it and returns the lines in a list

base = Path(__file__).parent
preset_dir = base / "presets"
text_file = preset_dir / "test.txt"


def load_file(path):

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.") # Checks if the path actually exists

    text = path.read_text()

    if text.strip() == "":
        raise FileNotFoundError(f"{path} is completely empty.")

    text_list = text.splitlines()

    return text_list

# Add a line to the preset file, but if the name is already present, replace the current one

def add_line(path, elements):

    # read_text().splitlines() handles empty files and strips the final newline
    lines = path.read_text().splitlines()

    new_line = ",".join(map(str, elements))

    for i in range(len(lines)):
        if lines[i].split(",")[0] == elements[0]:
            lines[i] = new_line
            break
            
    else:
        lines.append(new_line)

    path.write_text("\n".join(lines) + "\n")



if __name__ == "__main__":

    add_line(text_file, ["F-16", 999, 45000, 111, 222, 333, 444, 555, 1])


# Given a list of lines, find the line which represents the search term

def search_for_line(preset_list, target):

    if not preset_list:
        raise FileNotFoundError("File is empty.")

    for line in preset_list:

        preset = line.split(",")

        output_list = [preset[0]]
        output_list.extend(list(map(Decimal, preset[1:]))) # Turns all numbers into Decimal type
        
        if output_list[0] == target: # Target found

            from plane import PlaneConstants

            # return a PlaneConstants object built from the values
            plane_constants = PlaneConstants(
                name=output_list[0],
                lift_coefficient_gradient=output_list[1],
                lift_coefficient_intercept=output_list[2],
                drag_coefficient_gradient=output_list[3],
                drag_coefficient_intercept=output_list[4],
                wing_area=output_list[5],
                frontal_area=output_list[6],
                mass=output_list[7],
                thrust=output_list[8]
            )

            return plane_constants
        
    raise KeyError(f"Preset not in file list")


