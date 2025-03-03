import time
import pandas as pd


class retry(object):

    # Only works with DataFrames atm
    @classmethod
    def empty_dataframe(cls, func):
        def wrapper(*arguments,**kwargs):
            f = func(*arguments, **kwargs)
            while f.empty:
                func(*arguments,**kwargs)
                print('<<< Retrying >>>')
                time.sleep(1)
            return func(*arguments, **kwargs)
        return wrapper
