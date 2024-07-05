import os

from face_swapper import *
from runwayml_t2i import *

def eval_face_swapper():

  creat_face_swapper()

  source_dir = "./source/man/"
  face_img = "./source/face/man_face1.PNG"
  out_dir = "./output/" 

  for (i, img_dir) in enumerate(os.listdir("source_dir")):
    print("{i}th face swapping:______________________")
    img_path = source_dir + img_dir

    swap_one_image(img_path, face_img, out_dir + "face_swap_res_{i}.jpg")
    print("__finished____________________")

if __name__ == '__main__':
  print("Welcome to our Great Solutions!")

  eval_face_swapper()