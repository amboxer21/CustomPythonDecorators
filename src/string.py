#!/usr/bin/env python

import re

from Crypto import Random
from Crypto.Cipher import AES

class MetaString(type):

    def __new__(meta,name,bases,dct):
        if not hasattr(meta,'random'):
            meta.random = Random.new().read(16)
        return super(MetaString, meta).__new__(meta, name, bases, dct)

    def __init__(cls,name,bases,dct):
        if not hasattr(cls,'IV'):
            cls.IV = MetaString.random
        if not hasattr(cls,'KEY'):
            cls.KEY = MetaString.random
        if not hasattr(cls,'ciphertext'):
            cls.ciphertext = '\0'
        super(MetaString,cls).__init__(name,bases,dct)

class string(object):

    __metaclass__ = MetaString

    @classmethod
    def encrypt(cls,func):
        def wrapper(*arguments):
            if not re.match('<__main__.*object at.*>',str(arguments[0])):
                raise SyntaxError('Method must be an instance method of a class!')
            for arg in arguments[1:]:
                string.ciphertext = AES.new(string.KEY, AES.MODE_CFB, string.IV).encrypt(arg)
            return func(arguments[0].__class__,string.ciphertext)
            print string.KEY
        return wrapper

    @classmethod
    def decrypt(cls,func):
        def wrapper(*arguments):
            if not re.match('<__main__.*object at.*>',str(arguments[0])):
                raise SyntaxError('Method must be an instance method of a class!')
            for arg in arguments[1:]:
                string.ciphertext = AES.new(string.KEY, AES.MODE_CFB, string.IV).decrypt(arg)
            return func(arguments[0].__class__,string.ciphertext)
        return wrapper

class TestStringClass(object):

    @string.encrypt
    def encrypt(self,string):
        return string

    @string.decrypt
    def decrypt(self,string):
        return string

if __name__ == '__main__':

    # This will work
    test = TestStringClass()
    encrypted_text = test.encrypt('This is an encrypted string')
    print test.decrypt(encrypted_text)

# This will not work
@string.encrypt
def test_string_method(string):
    string

test_string_method('This is a test')
