import re
import os

def find_byte_sequence(file_path, byte_sequence):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Replace '??' with a regex pattern to match any two hexadecimal characters
    regex_pattern = byte_sequence.replace('??', r'(..)').replace(' ', '')

    match = re.search(regex_pattern, content.hex())
    if match:
        start_position = match.start() // 2  # Convert byte offset to character offset
        return start_position # Adjust for wildcard positions
    else:
        return None

def read_patterns_from_file(file_path):
    patterns = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                name, pattern = line.split('=')
                patterns[name.strip()] = pattern.strip()
    return patterns

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    patterns_file_path = os.path.join(script_directory, "patterns.txt")

    if not os.path.isfile(patterns_file_path):
        print("Error: patterns.txt not found in the script's directory.")
        exit(1)

    patterns = read_patterns_from_file(patterns_file_path)

    file_path = r"D:\Program Files (x86)\Steam\steamapps\common\Geometry Dash\GeometryDash.exe"

    for name, byte_sequence in patterns.items():
        address = find_byte_sequence(file_path, byte_sequence)
        if address is not None:
            print(f"{name}={hex(address)}")
        else:
            print(f"{name}=Byte sequence not found in the executable.")
