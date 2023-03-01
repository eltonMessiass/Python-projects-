# install all the libraries needed
# create a function that collect a text and converts it to a qr_code
# save the qr_code as an image
# run the function

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Enter your url: https://")
generate_qrcode(f"https://{url}")