import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

print()

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print()

registry = weakref.WeakValueDictionary()

first = Record()
second = Record()
temporary = Record()

registry["first"] = first
registry["second"] = second
registry["third"] = temporary

print("После регистрации:", list(registry.keys()))

del temporary
print("После удаления временной ссылки:", list(registry.keys()))

del second
print("После удаления второй сильной ссылки:", list(registry.keys()))