from diffusers import StableDiffusionPipeline

# Load Image Generation Model
image_model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

def generate_image(prompt):
    """Generate an image based on user prompt"""
    image = image_model(prompt).images[0]
    image.save("uploads/output.png")
    return "uploads/output.png
