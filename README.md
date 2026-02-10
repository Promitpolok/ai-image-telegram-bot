# 🎨 AI Image Generation Telegram Bot

A powerful Telegram bot that provides high-quality AI image generation services with text-to-image, image-to-image, image-to-text, and upscaling capabilities.

## ✨ Features

- **Text-to-Image Generation**: Create high-quality images from text descriptions using Stable Diffusion XL
- **Image-to-Image Transformation**: Transform existing images with AI-powered modifications
- **Image-to-Text**: 
  - Image Captioning: Generate descriptive text from images
  - OCR: Extract text from images
- **2K Upscaling**: Upscale images to 2K resolution while maintaining quality
- **Multiple Aspect Ratios**:
  - Square (1:1) - 1024x1024
  - Portrait (2:3) - 768x1152
  - Landscape (3:2) - 1152x768
  - Wide (16:9) - 1344x768
  - Ultra-wide (21:9) - 1536x640

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Hugging Face API Token (from [Hugging Face Settings](https://huggingface.co/settings/tokens))

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/Promitpolok/ai-image-telegram-bot.git
cd ai-image-telegram-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your tokens:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
HUGGING_FACE_TOKEN=your_hugging_face_token_here
```

4. **Run the bot**
```bash
python bot.py
```

## 🌐 Deploy to Hugging Face Spaces

### Step 1: Create a Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose:
   - **Name**: `ai-image-telegram-bot`
   - **SDK**: Docker
   - **Visibility**: Public or Private

### Step 2: Configure Secrets

In your Space settings, add these secrets:
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `HUGGING_FACE_TOKEN`: Your HF API token

### Step 3: Push Code

```bash
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/ai-image-telegram-bot
git push hf main
```

Your bot will be live globally 24/7! 🎉

## 📖 Usage

### Available Commands

- `/start` - Welcome message and feature overview
- `/generate` - Generate image from text description
- `/transform` - Transform an existing image
- `/caption` - Get AI-generated caption for an image
- `/ocr` - Extract text from an image
- `/upscale` - Upscale image to 2K resolution
- `/ratio` - Change aspect ratio preference
- `/help` - Show all commands and examples

### Example Usage

**Text-to-Image:**
```
1. Send /generate
2. Select your preferred aspect ratio
3. Type your prompt: "A serene mountain landscape at sunset, photorealistic"
4. Wait 30-60 seconds
5. Receive your high-quality image!
```

**Image-to-Image:**
```
1. Send /transform
2. Upload an image
3. Describe the transformation: "Make it look like a watercolor painting"
4. Get your transformed image!
```

**Image Captioning:**
```
1. Send /caption
2. Upload an image
3. Get AI-generated description
```

**OCR (Text Extraction):**
```
1. Send /ocr
2. Upload image with text
3. Get extracted text
```

**Upscaling:**
```
1. Send /upscale
2. Upload image
3. Get 2K upscaled version
```

## 🏗️ Architecture

### Technology Stack

- **Language**: Python 3.9+
- **Bot Framework**: python-telegram-bot (v20+)
- **AI Models**: Hugging Face Inference API
- **Image Processing**: Pillow (PIL)
- **OCR**: Tesseract OCR
- **Deployment**: Hugging Face Spaces (Docker)

### Models Used

- **Text-to-Image**: `stabilityai/stable-diffusion-xl-base-1.0`
- **Image-to-Image**: `timbrooks/instruct-pix2pix`
- **Image Captioning**: `Salesforce/blip-image-captioning-large`
- **Upscaling**: `caidas/swin2SR-realworld-sr-x4-64-bsrgan-psnr`

### Project Structure

```
ai-image-telegram-bot/
├── bot.py                 # Main bot application
├── handlers/
│   ├── __init__.py
│   ├── text_to_image.py  # Text-to-image handler
│   ├── image_to_image.py # Image-to-image handler
│   ├── image_to_text.py  # Captioning & OCR
│   └── upscale.py        # Upscaling handler
├── utils/
│   ├── __init__.py
│   ├── image_utils.py    # Image processing utilities
│   ├── api_client.py     # Hugging Face API client
│   └── constants.py      # Constants (ratios, models)
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── Dockerfile            # Docker configuration for HF Spaces
├── app.py                # Entry point for HF Spaces
├── README.md             # This file
└── .gitignore           # Git ignore file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather | Yes |
| `HUGGING_FACE_TOKEN` | HF API token for inference | Yes |
| `MAX_QUEUE_SIZE` | Maximum concurrent requests | No (default: 3) |
| `TIMEOUT` | Request timeout in seconds | No (default: 300) |

### Quality Settings

The bot uses high-quality default settings:
- **Guidance Scale**: 7.5-9 (controls prompt adherence)
- **Inference Steps**: 30-50 (more steps = higher quality)
- **Upscaling Factor**: 4x with quality preservation

## 🐛 Troubleshooting

### Common Issues

**Bot not responding:**
- Check if the bot is running (`python bot.py`)
- Verify your `TELEGRAM_BOT_TOKEN` is correct
- Check Hugging Face Spaces logs if deployed

**Image generation fails:**
- Verify your `HUGGING_FACE_TOKEN` is valid
- Check if you have enough HF API quota
- Try a simpler prompt
- Wait a bit and retry (servers might be busy)

**Upscaling timeout:**
- Large images take longer to upscale
- Try with smaller input images first
- Check your internet connection

**OCR not working:**
- Ensure Tesseract is installed: `sudo apt-get install tesseract-ocr`
- For Spaces, it's included in the Dockerfile

### Debug Mode

Enable logging to see detailed information:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📝 Getting Tokens

### Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot`
3. Follow the prompts to name your bot
4. Copy the token provided

### Hugging Face Token

1. Go to [Hugging Face](https://huggingface.co)
2. Sign up or log in
3. Go to Settings → [Access Tokens](https://huggingface.co/settings/tokens)
4. Create a new token with "Read" permissions
5. Copy the token

## 🌍 Global Availability

- Deployed on Hugging Face Spaces for 24/7 global availability
- No geographic restrictions
- Automatic restarts on failure
- Free tier available

## 📄 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Contact: @Promitpolok

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co) for providing free AI model inference
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot](https://python-telegram-bot.org) community

---

Made with ❤️ by [@Promitpolok](https://github.com/Promitpolok)