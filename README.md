# CustomPythonDecorators
Custom Python decorators I wrote to restrict method arguments to a specific type. If you pass an argument other than what the decorator allows it will raise a TypeError exception.

**Example:**

```python
class TestAcceptsClass(object):

    @accepts.boolean
    def _boolean(self,_boolean_):
        print('boolean => ', _boolean_)

    @accepts.integer
    def _integer(self,_integer_):
        print('integer => ', _integer_)

    @accepts.string
    def _string(self,_string_):
        print('string => ', _string_)

    @accepts.dictionary
    def _dictionary(self,_dictionary_):
        print('dictionary => ', _dictionary_)

    @accepts.list
    def _list(self,_list_):
        print('list => ', _list_)

    @accepts.tuple
    def _tuple(self,_tuple_):
        print('tuple => ', _tuple_)

if __name__ == '__main__':

    test = TestAcceptsClass()

    test._integer(1)
    test._integer(1,2)

    test._boolean(True)
    test._boolean(True,False)

    test._list(['1','2','3'])
    test._list(['1','2','3'],['4','5','6'])

    test._tuple(('1','2','3'),)
    test._tuple(('1','2','3'),('4','5','6'))

    test._string('test string')
    test._string('test string1','test string2')

    test._dictionary(
        {'one': '1','two': '2','three': '3'},
        {'one': '1','two': '2','three': '3'}
    )
    test._dictionary({'one': '1','two': '2','three': '3'})
```

> ^^ Remove newlines in between method declarations if using the python shell/interpretter and are having problems!
