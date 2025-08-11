# import qrcode
# #python -m pip install qrcode
# # Remove-Item -Recurse -Force .\__pycache__\
#
# data = "https://youtu.be/L-WOnGQRb3Q?si=AmCnd4JvoBj2E6Lb"
#
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(data)
# qr.make(fit=True)
#
# img = qr.make_image(fill_color='red', back_color='white')
# img.save('MyQRCode1.png')   # Saves the image
# img.show()                  # Displays the image in default viewer
import qrcode

img = qrcode.make("https://example.com")
img.save("my_qr_code.png")
print("QR code saved!")
