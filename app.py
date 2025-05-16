from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    # Debug: Log incoming files and form data
    print("==== Incoming Request ====")
    print("FILES:", request.files)
    print("FORM:", request.form)
    
    file = request.files.get('data')  # Must match n8n's form field name
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        # Read and OCR the image
        image = Image.open(file.stream)
        text = pytesseract.image_to_string(image)
        return jsonify({"text": text})

    except Exception as e:
        print("ERROR during OCR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
