#!/usr/bin/env python

import re

# Test cases have been added and this class should only be used with
# instance methods of a class. Using them outside of this case will
# result in undefined behavior and might not properly work as I have designed.

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
    def tuple(cls,func):
        arg_count = func.__code__.co_argcount
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not isinstance(args, tuple):
                    raise TypeError('"' + str(arg) + '" is not a tuple!')
                else:
                    if int(arg_count) > 1:
                        return func(cls,arg)
                    return func(arg)
        return wrapper
    
    # Needs fixing because return value is incorrect
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

    # Needs fixing because return value is incorrect
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

class TestAcceptsClass(object):

    @accepts.boolean
    def _boolean(_boolean_):
        print('boolean => ', _boolean_)

    @accepts.integer
    def _integer(_integer_):
        print('integer => ', _integer_)

    @accepts.string
    def _string(_string_):
        print('string => ', _string_)

    @accepts.dictionary
    def _dictionary(_dictionary_):
        print('dictionary => ', _dictionary_)

    @accepts.list
    def _list(_list_):
        print('list => ', _list_)

    @accepts.tuple
    def _tuple(_tuple_):
        print('tuple => ', _tuple_)

if __name__ == '__main__':
    test = TestAcceptsClass()
    test._integer(1)
    test._boolean(True)
    test._list(['1','2','3'])
    test._tuple(('1','2','3'))
    test._string('test string')
    test._dictionary({'one': '1','two': '2','three': '3'})
