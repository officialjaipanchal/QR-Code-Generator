
# Importing required library
import qrcode

def generate_qr_code(url, file_name="qr_code.png"):
    """
    This function generates a QR code for the provided URL
    and saves it as an image file.

    Parameters:
    url (str): The URL to encode in the QR code.
    file_name (str): The name of the output QR code image file.
    """

    # Creating a QR code object with custom settings
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of border (minimum is 4)
    )

    # Adding data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the image from QR Code object
    img = qr.make_image(fill_color="black", back_color="white")

    # Saving the QR code image to file
    img.save(file_name)

    print(f"QR Code generated and saved as {file_name}")

if __name__ == "__main__":
    # User Input for URL
    url_input = input("Enter the URL to generate QR Code: ")
    generate_qr_code(url_input)
