from datetime import datetime
import os
from PIL import Image
import time
from progress.bar import ChargingBar

start_time = datetime.now()

dir = os.path.abspath(r'\\fs\IM\photo_to_IM')
resize_dir = os.path.abspath(r'\\fs\IM\resized_im\{}') 
count = len([f for f in os.listdir(dir)])
bar = ChargingBar('Decoding', max=count)

for f in os.scandir(dir):
    if f.is_file() and f.path.split('.')[-1].lower() == 'jpg':
        if os.path.exists(resize_dir.format(f.name)):
            print(f"File {f.name} already exists. Skipping...")
        else:
            image = Image.open(f.path)
            image.save(resize_dir.format(f.name))
            bar.next()
            time.sleep(0.01)
bar.finish()        
print('All Done') 
print(datetime.now() - start_time)