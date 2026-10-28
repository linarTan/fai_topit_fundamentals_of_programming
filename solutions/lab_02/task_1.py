import copy

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = first[:]
print(first == second)
print(first is second)
second.append(40)
print(first)

print()

project1 = dict(name='fin1', members=['lin', 'naz'], l_pr=[['budget', 10000],['months', 6]])
project2 = project1
print("project1:", project1)
print("project2:", project2)
print("Один объект:", project1 is project2)
project2['l_pr'][0][1] = 20000
print("\nПосле изменения:")
print("project1:", project1)
print("project2:", project2)
print("Один объект:", project1 is project2)

print()

project1 = dict(name='fin1', members=['lin', 'naz'], l_pr=[['budget', 10000],['months', 6]])
project2 = copy.deepcopy(project1)
print("project1:", project1)
print("project2:", project2)
print("Один объект:", project1 is project2)
project2['l_pr'][0][1] = 20000
print("\nПосле изменения:")
print("project1:", project1)
print("project2:", project2)
print("Один объект:", project1 is project2)

print("\nПроверка объектов:")
print("Словари общие:", project1 is project2)
print("Списки участников общие:",
      project1['members'] is project2['members'])
print("Списки параметров общие:",
      project1['l_pr'] is project2['l_pr'])
print("Списки бюджета общие:",
      project1['l_pr'][0] is project2['l_pr'][0])

assert project1 is not project2
assert project1["l_pr"][0][1] == 10000
assert project2["l_pr"][0][1] == 20000
assert project1["members"] is not project2["members"]
