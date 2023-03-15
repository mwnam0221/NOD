import glob
from tqdm import tqdm 
import numpy as np
# img_list=glob.glob('./Nikon/*')

# print(img_list)

# img = [x.split('/') for x in img_list]
# print(img)
# temp = [str(x).split('.')[0]+'.JPG' for x in img_list]
# print(temp)


import rawpy
import imageio
import natsort

img_list=natsort.natsorted(glob.glob('./Nikon/*'))
img_names=[x.split('/')[-1].split('.')[0] for x in img_list]

for img_name, path in tqdm(zip(img_names, img_list)):    
    with rawpy.imread(path) as raw:
        # rgb = raw.postprocess()
        rgb = raw.raw_image
    
        imageio.imwrite('./Nikon_JPG/'  + f'/{img_name}.jpg', rgb.astype(np.uint16))    
