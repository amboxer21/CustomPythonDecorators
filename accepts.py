#!/usr/bin/env python

# Test cases have been added and this class should only be used with
# instance methods of a class. Using them outside of this case will
# result in an exception being raised. Using these custom decorators
# in conjunction with the staticclass decorators will result in undefined
# behavior because I have not tested this case and do not plan on it.

import re

class accepts(object):

    @classmethod
    def instancemethod(cls,func):
        def wrapper(*arguments):
            if not [arg for arg in arguments if re.match('<__main__.*object at.*>',str(arg))]:
                raise SyntaxError('Method must be an instance method of a class!')
            return func(arguments[1:])
        return wrapper

    @classmethod
    def boolean(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, bool):
                    raise TypeError('"' + str(arg) + '" is not a bool type!')
            return func(cls,arguments[0])
        return wrapper
    
    @classmethod
    def integer(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, int):
                    raise TypeError('"' + str(arg) + '" is not an integer!')
            return func(cls,arguments[0])
        return wrapper
    
    @classmethod
    def string(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, str):
                    raise TypeError('"' + str(arg) + '" is not a string!')
            return func(cls,arguments[0])
        return wrapper
    
    @classmethod
    def dictionary(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, dict):
                    raise TypeError('"' + str(arg) + '" is not a dictionary!')
            return func(cls,arguments[0])
        return wrapper
    
    @classmethod
    def list(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, list):
                    raise TypeError('"' + str(arg) + '" is not a list!')
            return func(cls,arguments[0])
        return wrapper
    
    @classmethod
    def tuple(cls,func):
        @accepts.instancemethod
        def wrapper(*arguments):
            for arg in arguments[1:]:
                if not isinstance(arg, tuple):
                    raise TypeError('"' + str(arg) + '" is not a tuple!')
            return func(cls,arguments[0])
        return wrapper
