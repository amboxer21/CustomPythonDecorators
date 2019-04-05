#!/usr/bin/env python

import re

from Crypto import Random
from Crypto.Cipher import AES

class MetaString(type):

    def __new__(meta,name,bases,dct):
        if not hasattr(meta,'random'):
            meta.random = Random.new()
        return super(MetaString, meta).__new__(meta, name, bases, dct)

    def __init__(cls,name,bases,dct):
        if not hasattr(cls,'IV'):
            cls.IV = MetaString.random.read(16)
        if not hasattr(cls,'KEY'):
            cls.KEY = MetaString.random.read(32)
        if not hasattr(cls,'ciphertext'):
            cls.ciphertext = '\0'
        super(MetaString,cls).__init__(name,bases,dct)

class string(object):

    __metaclass__ = MetaString

    @classmethod
    def instancemethod(cls,func):
        def wrapper(*arguments):
            if not re.match('<__main__.*object at.*>',str(arguments[0])):
                raise SyntaxError('Method must be an instance method of a class!')
            return func(arguments[0:])
        return wrapper

    @classmethod
    def encrypt(cls,func):
        @string.instancemethod
        def wrapper(*arguments):
            arguments = arguments[0]
            if not isinstance(arguments[1], str):
                raise TypeError('Argument is not of type Str!')
            string.ciphertext = AES.new(string.KEY, AES.MODE_CFB, string.IV).encrypt(arguments[1])
            return func(arguments[0].__class__,string.ciphertext)
        return wrapper

    @classmethod
    def decrypt(cls,func):
        @string.instancemethod
        def wrapper(*arguments):
            arguments = arguments[0]
            if not isinstance(arguments[1], str):
                raise TypeError('Argument is not of type Str!')
            string.ciphertext = AES.new(string.KEY, AES.MODE_CFB, string.IV).decrypt(arguments[1])
            return func(arguments[0].__class__,string.ciphertext)
        return wrapper
