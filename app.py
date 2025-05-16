from flask import Flask, request, jsonify
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    print("==== Incoming Request ====")
    print("FILES:", request.files)
    print("FORM:", request.form)

    file = request.files.get('data')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        pdf_bytes = file.read()

        # Convert PDF to images at lower DPI for faster rendering
        images = convert_from_bytes(pdf_bytes, dpi=120)

        # Use thread pool to parallelize OCR
        with ThreadPoolExecutor() as executor:
            results = executor.map(pytesseract.image_to_string, images)

        text = "\n".join(results)
        return jsonify({"text": text.strip()})

    except Exception as e:
        print("OCR ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
