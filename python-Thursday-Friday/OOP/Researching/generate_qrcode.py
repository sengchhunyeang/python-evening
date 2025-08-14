# animated_qrcode.py
#pip install qrcode-artistic

import segno
# from urllib.request import urlopen
from urllib.request import urlopen
salts_qrcode = segno.make_qr("")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
salts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)