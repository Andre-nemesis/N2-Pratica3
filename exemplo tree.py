from tree_2 import tree
t = tree(5)
t.insert(9)
t.insert(1)
t.insert(40)
t.insert(53)

print("Pré-ordem:")
t.pre_order()

print("In-ordem:")
t.in_order()

print("Pós-ordem:")
t.post_order()

print("Ordem de Níveis:")
t.level_order()

print(f'Representação:')
print(t.represent())