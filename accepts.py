#!/usr/bin/env python

# Call decorators with @Accepts.boolean, @Accepts.integer, etc. There are examples in the readme!
class Accepts(object):
    @staticmethod
    def boolean(func):
        def wrapper(*args):
            length = len(args)
            for index in range(1,(int(length))):
                if not str(args[int(index)]) in ('True','False'):
                    raise TypeError('"' + str(args[int(index)]) + '" is not a bool type!')
            return func
        return wrapper
    @staticmethod
    def integer(func):
        def wrapper(*args):
            length = len(args)
            for index in range(1,(int(length))):
                if re.search(r'\d+\b', args[int(index)]) is None:
                    raise TypeError('"' + str(args[int(index)]) + '" is not an integer!')
            return func
        return wrapper
