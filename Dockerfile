# Install system dependencies (Poppler, Tesseract, LibreOffice for .doc conversion)
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

# Expose the server port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
