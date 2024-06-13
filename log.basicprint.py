Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Print('hello world')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Print('hello world')
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print('hello world')
hello world
>>> name = 'Ex'
>>> lastname = 'Totoro'
>>> fullname = name +''+lastname
>>> prine(fullname)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    prine(fullname)
NameError: name 'prine' is not defined. Did you mean: 'print'?
>>> fullname = name + '' + lastname
>>> print(fullname)
ExTotoro
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Ex Totoro
>>> fullname=name+' '+lastname
>>> print(fullname)
Ex Totoro
>>> type(name)
<class 'str'>
>>> name,upper()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name,upper()
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> name.upper()
'EX'
>>> number=1
>>> print(number)
1
>>> number = '1'
>>> print(number)
1
>>> number.zfill(6)
'000001'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ขวบ'.format(name,lastname,age))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ขวบ'.format(name,lastname,age))
NameError: name 'age' is not defined
>>> age('10')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    age('10')
NameError: name 'age' is not defined
>>> age='10'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อEx นามสกุลTotoro อายุ10 ขวบ
