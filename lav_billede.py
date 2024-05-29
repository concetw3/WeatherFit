from PIL import Image
import os
import random
from toejprogram import outfit, timeseries
from datetime import datetime


outfit_liste = outfit(timeseries)


layout = {
    'skjorter': (0, 0), '1': (0, 1),'hovedbeklaedning': (0, 2), '3': (0, 3), 'jakker': (0, 4),
    'solbriller': (1, 0), '6': (1, 1), 't-shirts': (1, 2), '8': (1, 3), 'slips': (1, 4),
    'overtraeksbukser': (2, 0), '11': (2, 1), 'bukser_shorts': (2, 2), '13': (2, 3), 'handsker': (2, 4),
    'troejer': (3, 0), '16': (3, 1), 'sko': (3, 2), '18': (3, 3), 'baelter': (3, 4),
}


position_mapping = {
    'hovedbeklaedning' : 'hovedbeklaedning',
    'tshirt': 't-shirts',
    'bukser': 'bukser_shorts',
    'shorts': 'bukser_shorts',
    'sko': 'sko',
    'skjorter': 'skjorter',
    'jakker': 'jakker',
    'baelter': 'baelter',
    'troejer': 'troejer',
    'sweater': 'troejer',
    'overtraeksbukser': 'overtraeksbukser',
    'solbriller': 'solbriller',
    'handsker': 'handsker',  
}

print(outfit_liste)

cell_width = 1500
cell_height = 1500

grid_width = 5
grid_height = 4


grid_image = Image.new('RGB', (grid_width * cell_width, grid_height * cell_height), 'white')


'''outfit_liste = [
    {'name': 'Uponor kasket', 'category': 'hovedbeklaedning', 'image_path': './test_billeder/hat.jpg'},
    {'name': 'Bevar Christiania', 'category': 'tshirt', 'image_path': './test_billeder/metallica.jpg'},
    {'name': 'Ralph Lauren', 'category': 'skjorter', 'image_path':'./test_billeder/dolce_gabbana.jpg'},
    {'name': 'Helly Hansen regnjakke', 'category': 'jakker', 'image_path': './test_billeder/regnjakke.jpg'},
    {'name': 'Kentaur', 'category': 'bukser', 'image_path': './test_billeder/laederbukser.jpg'},
    {'name': 'metal baelte', 'category': 'baelter', 'image_path': './test_billeder/belt.jpg'},
    {'name': 'Colombia Sandaler', 'category': 'sko', 'image_path': './test_billeder/aquaman.jpg'}
]'''


position_images = {}


for item in outfit_liste:
    if item is None:
        continue  # Skip None values
    category = position_mapping.get(item['category'], None)
    if category and category in layout:
        pos = layout[category]
        img_path = item['image_path']
        if img_path and os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((cell_width, cell_height))
            if (pos, category) not in position_images:
                position_images[(pos, category)] = [img]
            else:
                position_images[(pos, category)].append(img)
        else:
            print(f"Failed to load image {img_path}: File not found.")


for (pos, category), images in position_images.items():
    if len(images) == 1:
        grid_image.paste(images[0], (pos[1] * cell_width, pos[0] * cell_height))
    else:  
        random_img = random.choice(images)
        grid_image.paste(random_img, (pos[1] * cell_width, pos[0] * cell_height))

filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'
grid_image.save(filename, 'JPEG')
grid_image.save('image_grid.jpg')
grid_image.show()
