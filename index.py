#import the necessary module!
from ensurepip import version
import urllib.parse
import flask
import qrcode
from PIL import Image
import matplotlib.pyplot as plt

texto = urllib.parse.quote_plus('''¡Hola! Nos conocimos en Andicom .Estoy interesado en conocer más de WeKall y Bidda. Espero tu respuesta.''')
input= 'https://api.whatsapp.com/send?phone=573105991006&text=%s' %texto
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(input)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('QrSandra.png')