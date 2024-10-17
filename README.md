# OCR
As part of my Enterprise Distributed Systems course, I implemented a simple web application to extract text from images using Optical Character Recognition (OCR).

There are two main components involved:
1. Python Flask application - This application handles the incoming requests containing the image from the UI, and uses the pytesseract library to extract the text from the image and returns the response.
2. UI webpage - This is a simple UI where you can upload images to be sent to the flask application, and it displays the extracted text.

Some sample images containing text are also present in the Sample Images folder.