import random
from werkzeug.security import generate_password_hash, check_password_hash
def generatorText():
    _upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _lower = 'abcdefghijklmnopqrstuvwxyz'
    _numbers = '0123456789'
    _special = '!@#$%^&*()'
    _simbols = '~`-_=+[{]}\\|;:\'",<.>/?'

    base = _upper + _lower + _numbers + _special 
    # base = _upper + _lower + _numbers + _special + _simbols
    long = 20
    shows = random.sample(base, long)
    password = ''.join(shows)
    encrypt = generate_password_hash(password)
    # print(password)
    print("{}   =>   {}   =>   {}".format(password, encrypt, check_password_hash(encrypt, password)))
    return {'password': password}
