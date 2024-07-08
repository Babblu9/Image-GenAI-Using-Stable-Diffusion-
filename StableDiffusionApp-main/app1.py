import tkinter as tk
from PIL import Image, ImageTk
import torch
from torch.cuda.amp import autocast
from diffusers import StableDiffusionPipeline
from accelerate import Accelerator

auth_token = "YOUR_HUGGING_FACE_TOKEN_HERE"

app = tk.Tk()
app.geometry("700x700")
app.title("Stable Bud")

prompt = tk.Entry(master=app, width=70, font=("Arial", 14))
prompt.place(x=10, y=10)

lmain = tk.Label(master=app, height=20, width=70)
lmain.place(x=10, y=110)

# Use the high-performance model, e.g., Stable Diffusion 2.1
model_id = "stabilityai/stable-diffusion-2-1"
device = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

accelerator = Accelerator()

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device != torch.device("cpu") else torch.float32, use_auth_token=auth_token)
pipe = accelerator.prepare(pipe.to(device))

def generate():
    input_text = prompt.get()
    with autocast(device.type):
        output = pipe(input_text, num_inference_steps=30, guidance_scale=7.5)
    
    print(output)
    
    image = output.images[0]
    image.save('generatedimage.png')

    img = Image.open('generatedimage.png')
    img = ImageTk.PhotoImage(img)
    lmain.configure(image=img)
    lmain.image = img

trigger = tk.Button(master=app, text="Generate", command=generate)
trigger.place(x=300, y=60)

app.mainloop()
