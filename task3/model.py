#Load the libraries
from diffusers import StableDiffusionPipeline
import torch

model_name = "hf-internal-testing/tiny-stable-diffusion-torch"
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16) #Load the model
prompt = "a photo of an astronaut riding a horse on mars" #input from user
image = pipe(prompt).images[0] #Generate image
image.save("astronaut.png") #Save image
image.show() #Show image