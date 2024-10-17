from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import base64
import io

# Set the path to the Tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Enable CORS for all domains on all routes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/perform-ocr', methods=['POST'])
def perform_ocr():
    
    if request.method == 'POST':
        # Handle actual OCR request
        data = request.get_json()
        image_data = data.get('image')

        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image)

        response = jsonify({"text": extracted_text})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response

if __name__ == '__main__':
    app.run(debug=True)