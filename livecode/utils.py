import hashlib
import hmac
import yaml
import qrcode


def sha1_encrypt(text):
    """sha1加密
    """
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()


def password_encrypt(password):
    """加盐hash密码"""
    key = b'livecode'
    h = hmac.new(key, password.encode('utf-8'), digestmod='sha1')
    return h.hexdigest()


def load_config(path):
    with open(path, 'r') as f:
        data = yaml.load(f)
    return data


def create_live_code(app, src):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=1,
    )
    qr.add_data(app['config']['domain'] + '/code_scan/' + src)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('./static/images/link/{}.png'.format(src))