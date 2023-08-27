from tree_2 import tree
t = tree(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)

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