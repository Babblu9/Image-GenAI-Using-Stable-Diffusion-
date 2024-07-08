# Image GenAI

Image GenAI is a desktop application that generates images from text prompts using the Stable Diffusion model. It utilizes the Tkinter library for the GUI and the Hugging Face `diffusers` library for generating images.

## Features

- Generate images from text prompts.
- Utilizes the Stable Diffusion 2.1 model for high-quality image generation.
- Easy-to-use graphical interface.

## Requirements

- Python 3.8 or higher
- Tkinter
- Pillow
- torch
- diffusers
- accelerate

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/stable-bud.git
    cd stable-bud
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install tkinter pillow torch diffusers accelerate
    ```

4. **Set up your Hugging Face authentication token:**

    Replace `"YOUR_HUGGING_FACE_TOKEN_HERE"` in the `app1.py` file with your actual Hugging Face authentication token.

## Usage

1. **Run the application:**

    ```bash
    python app1.py
    ```

2. **Enter a text prompt:**
   
   Type a description of the image you want to generate in the text entry box.

3. **Generate the image:**

   Click the "Generate" button to create an image based on your text prompt. The generated image will be displayed in the application window.

## Example

![Stable Bud Screenshot](screenshot.png)

## Troubleshooting

- Ensure you have the correct Hugging Face authentication token.
- Check that all required packages are installed.
- Ensure your system has a compatible GPU (CUDA or MPS) for faster image generation. The application will default to CPU if no compatible GPU is found.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the `diffusers` library and the Stable Diffusion model.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Pillow](https://python-pillow.org/) for image processing.

