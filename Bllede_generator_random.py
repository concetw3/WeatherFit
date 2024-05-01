from toejprogram3 import outfit, timeseries
import json
import os
import random
from PIL import Image, ImageOps
from datetime import datetime

outfit_liste = outfit(timeseries)
print(outfit_liste)
def get_billeder_from_names(names_list, json_file_paths):
    if names_list is None or not names_list:
        print("Warning: Received 'None' or empty list for names_list.")
        return {}

    image_dict = {}
    name_to_billede = {}

    for json_file_path in json_file_paths:
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                for key in possible_keys:
                    items = data.get(key, [])
                    for item in items:
                        if 'billede' in item and 'navn' in item:
                            name_to_billede[item['navn'].lower()] = item['billede']
        except FileNotFoundError:
            print(f"Error: The file {json_file_path} does not exist.")
        except json.JSONDecodeError:
            print(f"Error decoding the JSON in the file {json_file_path}.")
        except Exception as e:
            print(f"An unexpected error occurred while processing {json_file_path}: {e}")

    for name in names_list:
        normalized_name = name.lower()
        image_path = name_to_billede.get(normalized_name)
        if image_path:
            image_dict[name] = image_path


    
    image_dict = {image_path for _, image_path in image_dict.items()}
    return image_dict


possible_keys = [
    't-shirts', 'bukser', 'jakker', 'sko', 
    'skjorter', 'troejer', 'overtraeksbukser', 'huer', 'kasketter',
    'baelter', 'shorts'
]
json_files = ['./Json/accessories.json', './Json/bukser.json', './Json/hovedbeklaedning.json', './Json/jakker.json', './Json/sko.json', './Json/t-shirts.json', './Json/troejer.json',]

images_list = list(get_billeder_from_names(outfit_liste, json_files))
print(images_list)
#Resampling.LANCZOS
# image = Image.new('RGB', image_size, (255, 255, 255))


def concat_images(image_list, size, layout):
    width, height = size
    images = [Image.open(image_path) for image_path in images_list]
    images = [ImageOps.fit(image, size, Image.Resampling.LANCZOS) for image in images]
    
 
    max_row = max(layout.values(), key=lambda x: x[0])[0]
    max_col = max(layout.values(), key=lambda x: x[1])[1]
    image_size = (width * (max_col + 1), height * (max_row + 1))
    image = Image.new('RGB', image_size, (255, 255, 255))
    
 
    
    for idx in layout_keys:
        if idx < len(images):
            row, col = layout[idx]
            offset = width * col, height * row
            image.paste(images[idx], offset)
    
    return image


layout = {
    0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3), 4: (0, 4),
    5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3), 9: (1, 4),
    10: (2, 0), 11: (2, 1), 12: (2, 2), 13: (2, 3), 14: (2, 4),
    15: (3, 0), 16: (3, 1), 17: (3, 2), 18: (3, 3), 19: (3, 4),
}
layout_keys = list(layout.keys())
shuffled_images_list = images_list.copy() 
print(shuffled_images_list)
random.shuffle(shuffled_images_list)

new_layout = list(layout.keys())
random.shuffle(new_layout)
original_layout = layout.copy()
print(new_layout)
shuffled_layout = {new_layout[i]: original_layout[key] for i, key in enumerate(original_layout)}
filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'
print(shuffled_layout)
image = concat_images(images_list, (300, 300), shuffled_layout)
image.save(filename, 'JPEG')

