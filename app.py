from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files.get('data')  # <-- This now matches n8n's field
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        image = Image.open(file.stream)
        text = pytesseract.image_to_string(image)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
