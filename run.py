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

  target_face_dir = input("location of target face of character: ")
  size = 1024

  i = 0
  while True:
    i = i + 1
    print("_______________{i}th Generation_________________")
    
    prompt = input("prompt: ")
    if prompt == "finish":
      break

    negative_prompt = input("negative_prompt: ")

    out_dir = "./img/output/res_{i}.png"

    gen_res = generate_image_from_text(prompt, negative_prompt, size, out_dir)

    print("Image generated")

    if gen_res:
      out = swap_one_image(out_dir, target_face_dir,out_dir)
      if out:
        print("{i}th generation finished")
    



