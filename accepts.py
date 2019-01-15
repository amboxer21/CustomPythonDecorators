#!/usr/bin/env python

# Test cases have been added and this class should only be used with
# instance methods of a class. Using them outside of this case will
# result in undefined behavior and might not properly work as I have designed.

import re

class accepts(object):

    @classmethod
    def boolean(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, bool):
                    raise TypeError('"' + str(arg) + '" is not a bool type!')
                return func(cls,args[1:])
        return wrapper
    
    @classmethod
    def integer(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, int):
                    raise TypeError('"' + str(arg) + '" is not an integer!')
                return func(cls,args[1:])
        return wrapper
    
    @classmethod
    def string(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, str):
                    raise TypeError('"' + str(arg) + '" is not a string!')
                return func(cls,args[1:])
        return wrapper
    
    @classmethod
    def dictionary(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, dict):
                    raise TypeError('"' + str(arg) + '" is not a dictionary!')
                return func(cls,args[1:])
        return wrapper
    
    @classmethod
    def list(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, list):
                    raise TypeError('"' + str(arg) + '" is not a list!')
                return func(cls,args[1:])
        return wrapper
    
    @classmethod
    def tuple(cls,func):
        if int(func.__code__.co_argcount) < 2:
            raise SyntaxError('The '
                + str(func.__name__)
                + ' method must be an instance method of a class!')
        def wrapper(*args):
            for arg in args[1:]:
                if not isinstance(arg, tuple):
                    raise TypeError('"' + str(arg) + '" is not a tuple!')
                return func(cls,args[1:])
        return wrapper
