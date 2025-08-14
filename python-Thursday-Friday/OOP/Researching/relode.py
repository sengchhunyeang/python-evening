import segno

qrcode = segno.make("Hello, World")

qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("rotated_qrcode.png")