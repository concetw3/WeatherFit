import json

def load_json_file(path):
    with open(path) as f:
        return json.load(f)

# Load JSON data from files
file_paths = [
    './Json/accessories.json',
    './Json/hovedbeklaedning.json',
    './Json/bukser.json',
    './Json/solbriller.json',
    './Json/sko.json',
    './Json/troejer.json',
    './Json/jakker.json',
    './Json/t-shirts.json'
]

# Function to recursively extract names from JSON data
def extract_names(data):
    names = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    names.extend(extract_names(item))
            elif key == 'navn':
                names.append(value)
            else:
                names.extend(extract_names(value))
    elif isinstance(data, list):
        for item in data:
            names.extend(extract_names(item))
    return names

# List to store all names
all_names = []

# Load each JSON file and extract names
for path in file_paths:
    try:
        data = load_json_file(path)
        all_names.extend(extract_names(data))
    except Exception as e:
        print(f"Error loading {path}: {e}")

# Print all names
for name in all_names:
    print(name)
