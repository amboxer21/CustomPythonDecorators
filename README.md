# CustomPythonDecorators
Custom Python decorators I wrote. If you pass an argument other than what the decorator allows it will raise a TypeError exception.

**Example:**

```python
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
    # These test cases will work
    test = TestAcceptsClass()
    test._integer(1)
    test._boolean(True)
    test._list(['1','2','3'])
    test._tuple(('1','2','3'))
    test._string('test string')
    test._dictionary({'one': '1','two': '2','three': '3'})
```

> ^^ Remove newlines in between method declarations if using the python shell/interpretter and are having problems because you decided to add more example/test methods!
