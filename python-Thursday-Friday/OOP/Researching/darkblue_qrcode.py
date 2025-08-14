# darkblue_qrcode.py

import segno
var = input("drop link :")
qrcode = segno.make_qr(var)
qrcode.save(
    "darkblue_qrcode.png",
    scale=100,
    dark="pink",
)