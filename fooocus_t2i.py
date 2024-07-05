import os
import cv2
from replicate.client import Client
import env

replicate = None

def create_engine():
  replicate = Client(api_token={env.replicate_api})

def generate_image_from_text(prompt: str, negative_prompt: str, size: int, out_dir: str):
  """
  This is the main function of generating image from text.
  implemeted fooocus api for inferencing

  :param prompt: text to rely on generating image
         negative_prompt: features that to avoid when generating image
         size: size of generated image
         out: output location of generated image

  :return generated image

  """
  output = replicate.run(
    "konieshadow/fooocus-api-realistic:612fd74b69e6c030e88f6548848593a1aaabe16a09cb79e6d714718c15f37f47",
    input={
      "prompt": prompt,
      "cn_type1": "ImagePrompt",
      "cn_type2": "ImagePrompt",
      "cn_type3": "ImagePrompt",
      "cn_type4": "ImagePrompt",
      "sharpness": 2,
      "image_seed": 6091967260935476000,
      "uov_method": "Disabled",
      "image_number": 3,
      "guidance_scale": 3,
      "refiner_switch": 0.5,
      "negative_prompt": negative_prompt,
      "style_selections": "Fooocus V2,Fooocus Photograph,Fooocus Negative",
      "uov_upscale_value": 0,
      "outpaint_selections": "",
      "outpaint_distance_top": 0,
      "performance_selection": "Quality",
      "outpaint_distance_left": 0,
      "aspect_ratios_selection": "{size}*{size}",
      "outpaint_distance_right": 0,
      "outpaint_distance_bottom": 0,
      "inpaint_additional_prompt": ""
    }
  )

  cv2.imwrite(out_dir, output)

  return output

