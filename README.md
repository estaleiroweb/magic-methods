# Description

> Version: 0.0.1
> python 2.x,3.x

All Magic Methods Implement.

You can easyly to implement all magic methods or part of them

## Donate

**PIX**: +55 31 99101-8619

## Contact

**URL**: [http://estaleiroweb.com.br](http://estaleiroweb.com.br)

**GIT**: [https://github.com/HelbertFernandes/magic_methods](https://github.com/HelbertFernandes/magic_methods)

# Instalation

> pip install magic_methods

# Upgrade

> pip install magic_methods -upgrade

# Use

```python
from magicmethods import AllMethods

class MyClass(AllMethods): ...
```

```python
from magicmethods import AttributeMethods

class MyClass(AttributeMethods):
   def __init__(self):
      super().__init__()
      self._start_init()
      self.attr1 = 1
      self._end_init()

   def _set_value(self,val):
      self.__dict__['value']=val * 2

   def _set_attr2(self,val):
      self.__dict__['attr2']=val * 3

c = MyClass()
c.value = 2
c.attr1 = 2
c.attr2 = 2
c.attr3 = 2
print({'value': {'check': hasattr(c, 'value'), 'val': c.value}})
print({'attr1': {'check': hasattr(c, 'attr1'), 'val': c.attr1}})
print({'attr2': {'check': hasattr(c, 'attr2'), 'val': c.attr2}})
print({'attr3': {'check': hasattr(c, 'attr3')}})

'''Response: 
{'value': {'check': True, 'val': 4}}
{'attr1': {'check': True, 'val': 2}}
{'attr2': {'check': True, 'val': 6}}
{'attr3': {'check': False}}
'''
```

## MainMethods

Any classes bellow will inherit this class.

It implement then `__init__` method this `value` attribute.

The children classes must be the methods `_start_init()` and `_end_init()` to define attributes of class or if wish, you can not use `_end_init()` permiting add any attribute to this object

## MathMethods

Implement all Math magic methods

## FunctionMethods

Implement all Function magic methods

## LogicMethods

Implement all Logic magic methods

## BinaryMethods

Implement all Binary magic methods

## StringMethods

Implement all String magic methods

## CastMethods

Implement all Cast magic methods

## AttributeMethods

You can creating `_set_<attr>` methods to assure the correct value

## AllMethods

The same all classes above
