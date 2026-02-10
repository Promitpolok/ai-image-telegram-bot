"""
Entry point for Hugging Face Spaces deployment
"""

import os
import logging
from bot import main

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting AI Image Telegram Bot on Hugging Face Spaces...")
    
    # Verify tokens are set
    if not os.getenv("TELEGRAM_BOT_TOKEN"):
        logger.error("TELEGRAM_BOT_TOKEN not set!")
        exit(1)
    
    if not os.getenv("HUGGING_FACE_TOKEN"):
        logger.error("HUGGING_FACE_TOKEN not set!")
        exit(1)
    
    # Start the bot
    main()