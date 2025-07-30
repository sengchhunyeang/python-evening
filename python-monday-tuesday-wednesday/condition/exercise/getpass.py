import qrcode

data = "https://youtu.be/L-WOnGQRb3Q?si=AmCnd4JvoBj2E6Lb"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')
img.save('MyQRCode1.png')   # Saves the image
img.show()                  # Displays the image in default viewer
