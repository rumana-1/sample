Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("python is the general purpose interpretture,interactive,object\ oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM")
python is the general purpose interpretture,interactive,object\ oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM
>>> print("python is the general purpose interpretture,interactive,object\ oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM")
python is the general purpose interpretture,interactive,object\ oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM
>>> print("python is the general purpose interpretture,interactive,object\n oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM")
python is the general purpose interpretture,interactive,object
 oriented and high level programming langauge.it was created by GUIDO VAN ROSSUM
>>> print("check %3d",20)
check %3d 20
>>> d= 56
>>> print("check %3d",d)
check %3d 56
>>> print("check %3d"%d)
check  56
>>> print("check %7d"%d)
check      56
>>> b = 7
>>> print("check %7d %4d"%(d,b))
check      56    7
>>> 
print("check %7d %4d"%(d,b))
check      56    7
>>> 
>>> a=b/d
>>> b=9
>>> d=2
>>> a=b/d
>>> a=5/6
>>> 4/5
0.8
>>> b=2
>>> d=5
>>> a=b/d
>>> a=b/d
>>> a
0.4
>>> a = 4/67
>>> a
0.05970149253731343
>>> print("a is ",format(a,".3f"))
a is  0.060
>>> print("a is",format(a,".5f"))
a is 0.05970
>>> s=["a","b","c","d"]
>>> "c" in s
True
>>> "y" in s
False
>>> "y" not in s
True
>>> s.append(40)
>>> s
['a', 'b', 'c', 'd', 40]
>>> s.insert(1,python)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.insert(1,python)
NameError: name 'python' is not defined
>>> s.insert(1,"python")
>>> s
['a', 'python', 'b', 'c', 'd', 40]
>>> del s[3]
>>> s
['a', 'python', 'b', 'd', 40]
>>> s.sort()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> del s[4]
>>> s
['a', 'b', 'd', 'python']
>>> s.sort()
>>> s
['a', 'b', 'd', 'python']
>>> e=[12,45,77,23,54,78,55]
>>> e.sort()
>>> e
[12, 23, 45, 54, 55, 77, 78]
>>> a=s.append(e)
>>> a
>>> a = s.append(e)
>>> a
>>> del e
>>> e
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> s.reverse()
>>> s
[[12, 23, 45, 54, 55, 77, 78], [12, 23, 45, 54, 55, 77, 78], 'python', 'd', 'b', 'a']
>>> s
[[12, 23, 45, 54, 55, 77, 78], [12, 23, 45, 54, 55, 77, 78], 'python', 'd', 'b', 'a']
>>> a
>>> z=(12,13,14)
>>> z.append(34)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    z.append(34)
AttributeError: 'tuple' object has no attribute 'append'
>>> del z[1]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del z[1]
TypeError: 'tuple' object doesn't support item deletion
>>> z.insert(1,45)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    z.insert(1,45)
AttributeError: 'tuple' object has no attribute 'insert'
>>> z[0]
12
>>> e
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> s
[[12, 23, 45, 54, 55, 77, 78], [12, 23, 45, 54, 55, 77, 78], 'python', 'd', 'b', 'a']
>>> s[1]
[12, 23, 45, 54, 55, 77, 78]
>>> w=[[20,80,100],[34,76,100],[23,45,100]]
>>> w[0][2]
100
>>> z=(12,13,14)
>>> z=("we",1,"er",34,"sty")
>>> z[3]
34
>>> z[2]
'er'
>>> z[1] is 1
True
>>> 
>>> z[0] is "we"
True
>>> z[2] is 2
False
>>> 
