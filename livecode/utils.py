import hashlib
import hmac
import yaml


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