#!/usr/bin/env python

import re

from Crypto import Random
from Crypto.Cipher import AES

class string(object):

    encrypted_text = '\0'
    __KEY__  = Random.new().read(32)
    __IV__   = Random.new().read(16)

    @classmethod
    def encrypt(cls,func):
        def wrapper(*arguments):
            if not re.match('<__main__.*object at.*>',str(arguments[0])):
                raise SyntaxError('Method must be an instance method of a class!')
            for string in arguments[1:]:
                cls.encrypted_text = AES.new( cls.__KEY__, AES.MODE_CFB, cls.__IV__).encrypt(string)
            return func(arguments[0].__class__,cls.encrypted_text)
        return wrapper

    @classmethod
    def decrypt(cls,func):
        def wrapper(*arguments):
            if not re.match('<__main__.*object at.*>',str(arguments[0])):
                raise SyntaxError('Method must be an instance method of a class!')
            for string in arguments[1:]:
                cls.encrypted_text = AES.new( cls.__KEY__, AES.MODE_CFB, cls.__IV__).decrypt(string)
            return func(arguments[0].__class__,cls.encrypted_text)
        return wrapper
