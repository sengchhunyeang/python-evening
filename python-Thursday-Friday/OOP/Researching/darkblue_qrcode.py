# darkblue_qrcode.py
# https://realpython.com/python-generate-qr-code/
# python -m pip install segno
import segno
var = input("drop link :")
qrcode = segno.make_qr(var)
qrcode.save(
    "darkblue_qrcode.png",
    scale=100,
    dark="pink",
)