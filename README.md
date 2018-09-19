# CustomPythonDecorators
Custom Python decorators I wrote. If you pass an argument other than what the decorator allows it will raise a TypeError exception.

**Example:**

```python
class Test(object):
    def __init__(self):
        self.value = False
        
    @Accepts.boolean
    def test_func(self,value):
        self.value = value
   
if __name__ == '__main__':
    Test().test_func(False)   # This will work!
    Test().test_func('False') # This will fail!
```

^^ Remove newlines in between method declarations if using the python shell/interpretter!
