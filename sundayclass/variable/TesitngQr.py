# wide_border_qrcode.py

import segno

qrcode = segno.make_qr("https://pay.ababank.com/tzh3LCSZq83voz4R6")
qrcode.save(
    "ABA.png",
    scale=5,
    border=10,
)