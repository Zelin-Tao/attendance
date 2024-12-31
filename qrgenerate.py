import qrcode
import os

def generate_qr_code(url, save_path="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # QR_SIZE
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  # PIXEL_SIZE
        border=4, 
    )
    
    qr.add_data(url)
    qr.make(fit=True)


    img = qr.make_image(fill_color="black", back_color="white")

    # SAVE IN PATH
    os.makedirs(os.path.dirname(save_path), exist_ok=True) 
    img.save(save_path)
    print(f"QR Code SAVED IN: {save_path}")

#USE
generate_qr_code("https://forms.gle/sL4uC19q3uYu6Ee59", "C:/Users/tiosb/E2_qr.png")
