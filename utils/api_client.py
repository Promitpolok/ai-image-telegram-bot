"""
Hugging Face API client
"""

import os
import logging
import aiohttp
from typing import Optional

from utils.constants import MODELS, TEXT_TO_IMAGE_PARAMS, IMAGE_TO_IMAGE_PARAMS, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)

class HuggingFaceClient:
    """Client for Hugging Face Inference API."""
    
    def __init__(self):
        self.api_token = os.getenv("HUGGING_FACE_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
        self.timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
    
    async def text_to_image(self, prompt: str, width: int = 1024, height: int = 1024) -> bytes:
        """Generate image from text prompt."""
        url = f"https://api-inference.huggingface.co/models/{MODELS['text_to_image']}"
        
        payload = {
            "inputs": prompt,
            "parameters": {
                **TEXT_TO_IMAGE_PARAMS,
                "width": width,
                "height": height,
            }
        }
        
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            async with session.post(url, headers=self.headers, json=payload) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API Error: {error_text}")
                
                return await response.read()
    
    async def image_to_image(self, image_bytes: bytes, prompt: str) -> bytes:
        """Transform image based on prompt."""
        url = f"https://api-inference.huggingface.co/models/{MODELS['image_to_image']}"
        
        payload = {
            "inputs": prompt,
            "parameters": IMAGE_TO_IMAGE_PARAMS,
        }
        
        # For image-to-image, we need to send the image as well
        # This is a simplified version - you may need to adjust based on the model's API
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            data = aiohttp.FormData()
            data.add_field('file', image_bytes, filename='image.png', content_type='image/png')
            data.add_field('prompt', prompt)
            
            async with session.post(url, headers=self.headers, data=data) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API Error: {error_text}")
                
                return await response.read()
    
    async def image_to_text(self, image_bytes: bytes) -> str:
        """Generate caption for image."""
        url = f"https://api-inference.huggingface.co/models/{MODELS['image_captioning']}"
        
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            async with session.post(url, headers=self.headers, data=image_bytes) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API Error: {error_text}")
                
                result = await response.json()
                return result[0].get("generated_text", "No caption generated")
    
    async def upscale_image(self, image_bytes: bytes) -> bytes:
        """Upscale image to higher resolution."""
        url = f"https://api-inference.huggingface.co/models/{MODELS['upscaling']}"
        
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            async with session.post(url, headers=self.headers, data=image_bytes) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API Error: {error_text}")
                
                return await response.read()