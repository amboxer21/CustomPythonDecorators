class Accepts(object):
    
    @staticmethod
    def boolean(func):
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif not str(arg) in ('True','False'):
                    raise TypeError('"' + str(arg) + '" is not a bool type!')
            return func
        return wrapper
    
    @staticmethod
    def integer(func):
        def wrapper(*args):
            for arg in args:
                if re.search(r'<__main__',str(arg)) is not None:
                    pass
                elif re.search(r'\d+\b', str(arg)) is None:
                    raise TypeError('"' + str(arg) + '" is not an integer!')
            return func
        return wrapper
