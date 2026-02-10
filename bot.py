"""
AI Image Generation Telegram Bot
Main application entry point
"""

import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)
from dotenv import load_dotenv

from handlers.text_to_image import (
    start_text_to_image,
    handle_text_to_image_prompt,
    handle_ratio_selection,
)
from handlers.image_to_image import (
    start_image_to_image,
    handle_image_to_image_upload,
    handle_image_to_image_prompt,
)
from handlers.image_to_text import (
    start_caption,
    start_ocr,
    handle_caption_image,
    handle_ocr_image,
)
from handlers.upscale import start_upscale, handle_upscale_image

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = """
🎨 **Welcome to AI Image Generation Bot!**

I can help you create and modify images using advanced AI models.

**Available Features:**

🖼️ **Text-to-Image** - Generate images from descriptions
📸 **Image-to-Image** - Transform existing images
💬 **Image Captioning** - Get AI descriptions of images
📝 **OCR** - Extract text from images
⬆️ **Upscaling** - Enhance images to 2K resolution

**Commands:**
/generate - Create image from text
/transform - Modify an existing image
/caption - Get image description
/ocr - Extract text from image
/upscale - Upscale to 2K resolution
/ratio - Select aspect ratio
/help - Show detailed help

**Supported Aspect Ratios:**
• Square (1:1) - 1024x1024
• Portrait (2:3) - 768x1152
• Landscape (3:2) - 1152x768
• Wide (16:9) - 1344x768
• Ultra-wide (21:9) - 1536x640

Start by typing /generate or choose a command!
    """
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
📚 **Detailed Help Guide**

**1. Text-to-Image Generation** (/generate)
   • Type /generate
   • Select your preferred aspect ratio
   • Enter your text prompt
   • Wait 30-60 seconds
   • Receive your image!
   
   *Example prompt:* "A serene mountain landscape at sunset, photorealistic, 8k quality"

**2. Image-to-Image Transformation** (/transform)
   • Type /transform
   • Upload your image
   • Describe the transformation
   • Get your modified image!
   
   *Example:* "Make it look like a watercolor painting"

**3. Image Captioning** (/caption)
   • Type /caption
   • Upload an image
   • Get AI-generated description

**4. OCR - Text Extraction** (/ocr)
   • Type /ocr
   • Upload image with text
   • Get extracted text

**5. Image Upscaling** (/upscale)
   • Type /upscale
   • Upload image
   • Get 2K upscaled version

**6. Change Aspect Ratio** (/ratio)
   • Select preferred ratio for image generation

**Tips for Best Results:**
✨ Be specific and descriptive in prompts
✨ Use quality keywords like "8k", "detailed", "professional"
✨ For transformations, clearly describe desired style
✨ High-quality input images produce better results

**Limitations:**
⚠️ Generation may take 30-60 seconds
⚠️ Maximum file size: 20MB
⚠️ Some content may be filtered by AI safety systems

Need more help? Contact @Promitpolok
    """
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")
    
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "❌ An error occurred. Please try again or contact support."
        )


def main() -> None:
    """Start the bot."""
    # Get token from environment
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Text-to-Image handlers
    application.add_handler(CommandHandler("generate", start_text_to_image))
    application.add_handler(CommandHandler("ratio", start_text_to_image))
    application.add_handler(CallbackQueryHandler(handle_ratio_selection, pattern="^ratio_"))
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND & filters.UpdateType.MESSAGE,
            handle_text_to_image_prompt
        )
    )
    
    # Image-to-Image handlers
    application.add_handler(CommandHandler("transform", start_image_to_image))
    
    # Image-to-Text handlers
    application.add_handler(CommandHandler("caption", start_caption))
    application.add_handler(CommandHandler("ocr", start_ocr))
    
    # Upscale handler
    application.add_handler(CommandHandler("upscale", start_upscale))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()