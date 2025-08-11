import qrcode
#python -m pip install qrcode[pil]
# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data
qr.add_data('https://example.com')
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color='black', back_color='white')
img.save('example_qr.png')
