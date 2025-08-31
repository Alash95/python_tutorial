"""
QR Code Generator
This script generates a QR code from a given URL/Text and saves it as an image file.

Pseudo Code:
1. Import necessary libraries:
    - qrcode
    - PIL (Pillow)
2. Define a function `generate_qr_code(data, filename)`:
    a. Create a QR code object using `qrcode.QRCode()`
    b. Add data to the QR code using `qr.add_data(data)`
    c. Make the QR code with `qr.make(fit=True)`
    d. Create an image from the QR code using `qr.make_image()`
    e. Save the image to a file using `image.save(filename)
3. If this script is run directly, call `generate_qr_code()` with a sample URL/Text and filename.
"""

import qrcode
import PIL

data = input("Enter the text or URL: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

fill = input("Enter the fill colour of your choice: ")
background =  input("Enter the background colour of your choice: ")

img = qr.make_image(fill_color=fill, back_color=background)

file_name = input("Enter the filename with a .png appended: ")

img.save(file_name)
    