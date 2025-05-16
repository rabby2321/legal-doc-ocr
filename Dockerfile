FROM python:3.10-slim

# Install system dependencies (for OCR + .doc to .docx conversion)
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libreoffice \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
