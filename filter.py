from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join
import shutil

raw_images_path = 'images'

filtered_images_path = 'filtered-images'
# Clear the contents of the dir to which images are copied to.
shutil.rmtree(filtered_images_path, ignore_errors=True)
makedirs(filtered_images_path)

# We can provide a list of colors to search for. Thus, it is possible for us to search for different shades of a color.
colors_to_search_for = [(28, 28, 28)]

image_files = [join(raw_images_path, f) for f in listdir(raw_images_path) if isfile(join(raw_images_path, f))]

for image_name in image_files:
    image = Image.open(image_name).convert("RGB")
    colors = [count_color[1] for count_color in image.getcolors()]
    # if the the 2 lists have any common colors copy the image to the filtered img dir
    if bool(set(colors_to_search_for) & set(colors)):
        shutil.copy2(image_name, filtered_images_path)
