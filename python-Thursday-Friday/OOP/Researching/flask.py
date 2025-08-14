import segno
import io
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="get" action="/qrcode">
            <input type="text" name="link" placeholder="Enter link" required>
            <button type="submit">Generate QR</button>
        </form>
    '''

@app.route('/qrcode')
def generate_qrcode():
    link = request.args.get('link')
    qrcode = segno.make_qr(link)
    buffer = io.BytesIO()
    qrcode.save(buffer, kind='png', scale=10, dark="pink")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
