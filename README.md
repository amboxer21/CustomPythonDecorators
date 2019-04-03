# CustomPythonDecorators
These are custom Python decorators I wrote to restrict method arguments to a specific type. If you pass an argument other than what the decorator allows, it will raise a TypeError exception. These decorators also ensure that you are calling the decorator on an instance method of a class.

**Examples:**

>**accepts decorators**

```python
class TestAcceptsClass(object):

    # This instance method will raise an exception
    # if an argument other than boolean is passed.
    @accepts.boolean
    def _boolean(self,_boolean_):
        print('boolean => '+str(_boolean_))

    # This instance method will raise an exception
    # if an argument other than integer is passed.
    @accepts.integer
    def _integer(self,_integer_):
        print('integer => '+str(_integer_))

    # This instance method will raise an exception
    # if an argument other than string is passed.
    @accepts.string
    def _string(self,_string_):
        print('string => '+str(_string_))

    # This instance method will raise an exception
    # if an argument other than dict is passed.
    @accepts.dictionary
    def _dictionary(self,_dictionary_):
        print('dictionary => '+str(_dictionary_))

    # This instance method will raise an exception
    # if an argument other than list is passed.
    @accepts.list
    def _list(self,_list_):
        print('list => '+str(_list_))

    # This instance method will raise an exception
    # if an argument other than tuple is passed.
    @accepts.tuple
    def _tuple(self,_tuple_):
        print('tuple => '+str(_tuple_))

if __name__ == '__main__':

    # Our test class
    test = TestAcceptsClass()

    # The following examples are ways that the custom
    # decorators can be used. 
    
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
        {'four': '4','five': '5','six': '6'}
    )
    test._dictionary({'one': '1','two': '2','three': '3'})
    
    # The following test cases will fail and will raise a type exception!
    test._integer('1')
    test._integer('1','2')
    test._boolean(1)
    test._boolean('True','False',1)
    test._list(('1','2','3'))
    test._list(('1','2','3'),('4','5','6'))
    test._tuple(['1','2','3'],)
    test._tuple(['1','2','3'],['4','5','6'])
    test._string(True)
    test._string(True,False)

# The following examples will fail and will raise a SyntaxError
# and complain about the method not being an instance of a class.
@accepts.integer
def _integer(_integer_):
    print('integer: '+str(_integer_))
    
_integer(1)
    
```

>**encryption decorators**

```javascript
class TestStringClass(object):

    @string.encrypt
    def encrypt(self,string):
        return string 

    @string.decrypt
    def decrypt(self,string):
        return string

if __name__ == '__main__':

    # This will work
    test = TestString()
    encrypted_text = test.encrypt('This is an encrypted string')
    print test.decrypt(encrypted_text)

# This will not work
@string.encrypt
def test_string_method(string):
    string
    
test_string_method('This is a test')    
```

> ^^ Remove newlines in between method declarations if using the python shell/interpretter and are having problems!
