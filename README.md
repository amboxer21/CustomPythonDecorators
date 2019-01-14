# CustomPythonDecorators
Custom Python decorators I wrote. If you pass an argument other than what the decorator allows it will raise a TypeError exception. These decorators need a lot of work!

**Example:**

```python
class TestAcceptsClass(object):       
    @accepts.boolean
    def _boolean(_boolean_):
        print('boolean => ', _boolean_)
   
if __name__ == '__main__':
    test = TestAcceptsClass()
    test._boolean(True)    # This will work!
    test._boolean(False)   # This will work!
    test._boolean('False') # This will fail!
```

> ^^ Remove newlines in between method declarations if using the python shell/interpretter and are having problems because you decided to add more example/test methods!
