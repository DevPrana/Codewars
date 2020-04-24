import string
from codecs import encode as _dont_use_this_

def rot13(message):
    intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    trantab = string.maketrans(intab, outtab)
    return message.translate(trantab)
