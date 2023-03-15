import json
from pathlib import Path
from tqdm import tqdm
import PIL.Image as Image
import rawpy
import imageio
import numpy as np


file_name = 'raw_new_Nikon750_train'
output_file_name = 'images_train'

#1. get samples_train and samples_val
# Opening JSON file to read sample.json
f = open(f'/hdd/dan/NOD/RAW-NOD/annotations/Nikon/{file_name}.json', mode='r')  
##################
#(Nikon)train 3206, val 400 , test 400 total 4006 
#(Sony)train 2571  val 321 test 321 total 3213
#################
# returns JSON object as a dictionary
samples_train = json.load(f)    #each sample is an annotated image basically
# print(samples_train.keys()) #dict_keys(['info', 'licenses', 'images', 'categories', 'annotations'])
# Closing file
f.close()

#2. create list of images_json

images_train = samples_train.get('images')
print(images_train)
print(len(images_train)) #3206

# #3. create list of categories using dict.get('key')
categories_dict = samples_train.get('categories') #categories_dict is an array of dictionaries  #person(1), bicycle(2), car(3)
# print(categories_dict)


categories = []
for d in categories_dict:
  categories.append(d['name'])

#4. create annotations for train and val
annotations_train = samples_train.get('annotations')

#5. create_dataset function
#yolov5 format is <class_index> bbox_x_center bbox_y_center bbox_width bbox_height
def create_dataset(dataset_type, annotations, images_json):
  IMG_W = 3936
  IMG_H = 2624
  images_path = Path(f"./{dataset_type}/images")
  images_path.mkdir(parents=True, exist_ok=True)

  labels_path = Path(f"./{dataset_type}/labels")
  labels_path.mkdir(parents=True, exist_ok=True)

  for img_id, row in enumerate(tqdm(images_json)):
    #img_id is 0 to n, row is just an element in images_json
    img_id = row['id']
  
    path = './Nikon/' + row['file_name']
    #method2: original   
    with rawpy.imread(path) as raw: #.NEF
      rgb = raw.raw_image
      imageio.imwrite(f'./{dataset_type}'+'/images'  + f'/{img_id}.jpg', rgb.astype(np.uint16))    

    label_name = f"{dataset_type}_{img_id}.txt"
    
    with (labels_path / label_name).open(mode="w") as label_file: 
      # category_token = ''     
      for obj_anno in annotations:  #write all annotations and category for this image using object_ann.json
        if img_id == obj_anno['image_id']:
          # label = ''
          #get bounding box
          b_box = obj_anno['bbox']
          x_min, y_min, w, h = b_box[0], b_box[1], b_box[2], b_box[3]
          #normalized the data
          w_norm = w / IMG_W 
          h_norm = h / IMG_H
          x_cent_norm = (x_min + w/2) / IMG_W
          y_cent_norm = (y_min + h/2) / IMG_H

          #get category id
          category_idx = obj_anno['category_id'] - 1 # minus 1 because annotation in json start at 1 but list start at 0  
              
          label_file.write(f"{category_idx} {x_cent_norm} {y_cent_norm} {w_norm} {h_norm}\n")

#6. call create_dataset(dataset_type, annotations, images_json):
create_dataset(output_file_name, annotations_train, images_train) # samples_train is samples
