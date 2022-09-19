import pyqrcode

def gen_qr(s, name):
    pyqrcode.create(s).png('static/'+name, scale = 6)