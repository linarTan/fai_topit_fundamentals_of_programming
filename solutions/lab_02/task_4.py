import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Автоматическая сборка включена:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

first_id = id(first)
second_id = id(second)

print("Идентификаторы списков:", first_id, second_id)

del first
del second

collected = gc.collect()
print("Результат сборки:", collected)


gc.disable()

try:
    for i in range(3):
        first = []
        second = []

        first.append(second)
        second.append(first)

        del first
        del second

    collected = gc.collect()
    print("Результат ручной сборки при отключённой автоматической:", collected)
finally:
    gc.enable()


before = gc.collect()
print("Результат сборки до создания графа:", before)

node_a = {"name": "A", "links": []}
node_b = {"name": "B", "links": []}
node_c = {"name": "C", "links": []}
node_d = {"name": "D", "links": []}

node_a["links"].append(node_b)
node_b["links"].append(node_c)
node_c["links"].append(node_a)

print("A ссылается на B:", node_a["links"][0] is node_b)
print("B ссылается на C:", node_b["links"][0] is node_c)
print("C ссылается на A:", node_c["links"][0] is node_a)
print("Связи независимого узла D:", node_d["links"])

del node_a
del node_b
del node_c

after = gc.collect()

print("Результат сборки до создания графа:", before)
print("Результат сборки после удаления внешних имён:", after)

assert node_d["name"] == "D"
assert node_d["links"] == []

print("Независимый узел доступен:", node_d)