import streamlit as st
from PIL import Image
import torch
from torch.cuda.amp import autocast
from diffusers import StableDiffusionPipeline
from accelerate import Accelerator

auth_token = "YOUR_HUGGING_FACE_TOKEN_HERE"

st.title("IMAGE GEN AI")

prompt = st.text_input("Enter your prompt here:")

model_id = "CompVis/stable-diffusion-v1-4"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
st.write(f"Using device: {device}")

accelerator = Accelerator()

pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32, 
    use_auth_token=auth_token
)
pipe = accelerator.prepare(pipe.to(device))

def generate_image(input_text):
    with autocast(device.type):
        output = pipe(input_text, num_inference_steps=30, guidance_scale=7.5)
    return output.images[0]

if st.button("Generate"):
    if prompt:
        with st.spinner('Generating image...'):
            image = generate_image(prompt)
            st.image(image, caption='Generated Image', use_column_width=True)
    else:
        st.warning("Please enter a prompt.")
