# CustomPythonDecorators(That dont really work as they should)
Custom Python decorators I wrote. If you pass an argument other than what the decorator allows it will raise a TypeError exception. These decorators need a lot of work!

**Example:**

```python
class Test(object):       
    @Accepts.boolean
    def test_func(self,value):
        if value:
            print('Value passed is True')
        else:
            print('Value passed is False')
   
if __name__ == '__main__':
    Test().test_func(True)   # This will work!
    Test().test_func(False)   # This will work!
    Test().test_func('False') # This will fail!
```

> ^^ Remove newlines in between method declarations if using the python shell/interpretter and are having problems because you decided to add more example/test methods!
