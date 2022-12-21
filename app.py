from flask import Flask, render_template, request, send_file
import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/convert", methods=['GET'])
def convertUrlToQR():
    colors={'white':(255, 255, 255) , 'black':(0,0,0), 'blue':(65,105,225), 'red':(228,88,88), 'purple':(139,0,139)}
    url_for_qr = request.args.get('url_for_qr')
    bgColor = (request.args.get('bg-color')).split("-")[0]
    centerColor = (request.args.get('center-color')).split("-")[0]
    edgeColor = (request.args.get('edge-color')).split("-")[0]
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
    qr.add_data(url_for_qr)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(back_color=colors[bgColor], center_color=colors[centerColor], edge_color=colors[edgeColor]))
    fn = (str(url_for_qr)).split("https://")[1].split(".")[1]
    img.save('./static/qrs/' + fn + ".png")
    return render_template("convert.html", fn=fn, url_for_qr=url_for_qr)


@app.route('/download/<path:filename>', methods=['POST', 'GET'])
def downloadFile(filename):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path =  'static\\qrs\\' + filename + ".png"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False)
