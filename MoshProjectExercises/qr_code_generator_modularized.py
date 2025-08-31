"""QR Code Generator"""

import qrcode

def collect_inputs():
    """
    Prompt the user for the data to encode and styling options.
    Returns:
        tuple: (data, fill_color, back_color, filename)
    """
    data = input("Enter the text or URL: ").strip()
    fill_color = input("Enter the fill color of your choice: ").strip()
    back_color = input("Enter the background color of your choice: ").strip()
    filename = input("Enter the filename with a .png extension: ").strip()
    return data, fill_color, back_color, filename

def configure_qr(data, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4):
    """
    Create and configure a QRCode object.
    Args:
        data (str): The text or URL to encode.
        version (int): QR code version (size).
        error_correction: Error correction level.
        box_size (int): Pixel size of each box.
        border (int): Border thickness.
    Returns:
        qrcode.QRCode: Configured QR code object.
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr

def render_image(qr_obj, fill_color, back_color):
    """
    Generate a PIL image from the QR code object.
    Args:
        qr_obj (qrcode.QRCode): The QR code object.
        fill_color (str): Color for the code modules.
        back_color (str): Background color.
    Returns:
        PIL.Image.Image: The rendered QR code image.
    """
    while True:
        try:
            image = qr_obj.make_image(fill_color=fill_color, back_color=back_color)
            return image
        except Exception as e:
            print(f"⚠️  Invalid color choice ({e}).")
            fill_color = input("Enter a valid fill color: ")
            back_color = input("Enter a valid background color: ")

def save_image(image, filename):
    """
    Save the PIL image to disk, handling errors.
    Args:
        image (PIL.Image.Image): The QR code image.
        filename (str): Desired output filename.
    """
    try:
        image.save(filename)
        print(f"✅ QR code saved to {filename}")
    except Exception as e:
        print(f"❌ Failed to save image '{filename}': {e}")


def main():
    # Orchestrate the full flow
    data, fill_color, back_color, filename = collect_inputs()
    qr = configure_qr(data)
    img = render_image(qr, fill_color, back_color)
    save_image(img, filename)

if __name__ == "__main__":
    main()