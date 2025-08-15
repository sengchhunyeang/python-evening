# darkblue_qrcode.py
# https://realpython.com/python-generate-qr-code/
# python -m pip install segno
import segno
qrcode = segno.make_qr("https://github.com/sengchhunyeang/python-evening.git")
qrcode.save(
    "darkblue_qrcode.png",
    scale=80,
    dark="pink",
)