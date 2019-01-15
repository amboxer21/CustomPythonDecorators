#!/usr/bin/env python

# Test cases have been added and this class should only be used with
# instance methods of a class. Using them outside of this case will
# result in undefined behavior and might not properly work as I have designed.

import re

class accepts(object):

    @classmethod
    def boolean(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, bool):
                    raise TypeError('"' + str(arg) + '" is not a bool type!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
    
    @classmethod
    def integer(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, int):
                    raise TypeError('"' + str(arg) + '" is not an integer!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
    
    @classmethod
    def string(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, str):
                    raise TypeError('"' + str(arg) + '" is not a string!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
    
    @classmethod
    def dictionary(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, dict):
                    raise TypeError('"' + str(arg) + '" is not a dictionary!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
    
    @classmethod
    def list(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, list):
                    raise TypeError('"' + str(arg) + '" is not a list!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
    
    @classmethod
    def tuple(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(arg, tuple):
                    raise TypeError('"' + str(arg) + '" is not a tuple!')
            if int(arg_count) > 1:
                return func(cls,args)
            return func(args)
        return wrapper
