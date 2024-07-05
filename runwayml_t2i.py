"""

Text-to-Image

from hugginface.co runwayml

prompt example:

  prompt = "a young man running, listening music with ear phone, looking front, smiling, wearing red jacket and black pants, white and slim, front-photo, whole-phase"
n_prompt = "unrealistic, saturated, high contrast, painting, drawing, sketch, cartoon, anime, manga, render, 3d, watermark, signature, label"

"""
import io
import requrest
import matplotlib.pyplot as plt
from PIL import Image


# Set up the Hugging Face Inference API endpoint
api_endpoint = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

# Set up the API headers
headers = {
    "Authorization": "Bearer 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"
}

def generate_image_from_text(prompt: str, negative_prompt: str, size: int, out: str):
  """
  This is the main function of generating image from text.
  implemeted huggingface api for inferencing

  :param prompt: text to rely on generating image
         negative_prompt: features that to avoid when generating image
         size: size of generated image
         out: output location of generated image

  :return generated image
  """
    
  # Send the request to the Hugging Face Inference API
  payload = {
    "inputs": prompt,
    "negative_prompt":negative_prompt,
    "options": {
        "wait_for_model": True,
        "size": (size, size)
    }
  }    

  response = requests.post(api_endpoint, headers=headers, json=payload)

  # Check the response status code
  if response.status_code == 200:
    # Get the generated image data
    image_data = response.content

    # Save the generated image
    with open("generated_human_image.png", "wb") as f:
        f.write(image_data)

    # Display the generated image
    image = Image.open(io.BytesIO(image_data))
    plt.imshow(image)

    image.save(out)
    
    return image
  
  else:
    print(f"Error: {response.status_code} - {response.text}")

    return None




