import pyqrcode
from PIL import Image
link = input("Enter what you want to generate QR:")
qr_code = pyqrcode.create(link)
qr_code.png("QRcode.png", scale=5)
Image.open("QRcode.png)
