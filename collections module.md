# collections
## Counter
这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，
但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且
就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
```python
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
d                 #output:defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
list(d.items())   #output:[('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])]
