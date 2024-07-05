"""

Face2Face for faceswapper

"""

import cv2
from face2face import Face2Face

f2f_engine = None

def creat_face_swapper():
  """ Create Face Swapper Engine
  """
  f2f_engine = Face2Face()

def swap_one_image(src_img: str, target_face: str, out: str):
  """ 
  Swap face from source image compare to target face image

  :param src_img: source image location 
         target_face: target face image location
         out: save location of generated image

  """
  swapped_img = f2f_engine.swap_one_image(cv2.imread(src_img), cv2.imread(target_face))
  cv2.imwrite(out, swapped_img)

