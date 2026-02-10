"""
Constants and configuration
"""

# Aspect ratios for image generation
ASPECT_RATIOS = {
    "square": {
        "name": "Square 1:1",
        "width": 1024,
        "height": 1024,
    },
    "portrait": {
        "name": "Portrait 2:3",
        "width": 768,
        "height": 1152,
    },
    "landscape": {
        "name": "Landscape 3:2",
        "width": 1152,
        "height": 768,
    },
    "wide": {
        "name": "Wide 16:9",
        "width": 1344,
        "height": 768,
    },
    "ultrawide": {
        "name": "Ultra-wide 21:9",
        "width": 1536,
        "height": 640,
    },
}

# Hugging Face model endpoints
MODELS = {
    "text_to_image": "stabilityai/stable-diffusion-xl-base-1.0",
    "image_to_image": "timbrooks/instruct-pix2pix",
    "image_captioning": "Salesforce/blip-image-captioning-large",
    "upscaling": "caidas/swin2SR-realworld-sr-x4-64-bsrgan-psnr",
}

# Generation parameters
TEXT_TO_IMAGE_PARAMS = {
    "guidance_scale": 7.5,
    "num_inference_steps": 30,
}

IMAGE_TO_IMAGE_PARAMS = {
    "guidance_scale": 7.5,
    "num_inference_steps": 30,
    "strength": 0.8,
}

# Timeout settings
REQUEST_TIMEOUT = 300  # 5 minutes
MAX_QUEUE_SIZE = 3
"""