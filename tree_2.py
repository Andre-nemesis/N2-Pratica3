class node:
    def __init__(self, valor):
        self.value = valor
        self.left = None
        self.right = None
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.value, self.value, self.right and self.right.value)

class tree:
    def __init__(self, valor=None):
        self.raiz = node(valor)
    
    def _inserir(self, value, no):
        if no.left is None:
            no.left = node(value)
        elif no.right is None:
            no.right = node(value)
        else:
            if no.left.right is None:
                self._inserir(value, no.left)
            else:
                self._inserir(value, no.right)
        
    def insert(self, value):
        if self.raiz is None:
            self.raiz = node(value)
        else:
            self._inserir(value, self.raiz)

    def _preorder(self, no):
        if no:
            print(no.value, end=" - ")
            self._preorder(no.left)
            self._preorder(no.right)
    
    def pre_order(self):
        self._preorder(self.raiz)
        print()

    def _inorder(self, no):
        if no:
            self._inorder(no.left)
            print(no.value, end=" > ")
            self._inorder(no.right)
    
    def in_order(self):
        self._inorder(self.raiz)
        print()

    def _postorder(self, no):
        if no:
            self._postorder(no.left)
            self._postorder(no.right)
            print(no.value, end=" -> ")
    
    def post_order(self):
        self._postorder(self.raiz)
        print()

    def level_order(self):
        if self.raiz is None:
            return
        
        nos = [self.raiz]
        while nos:
            no = nos.pop(0)
            print(no.value, end=" <-> ")
            if no.left:
                nos.append(no.left)
            if no.right:
                nos.append(no.right)
        print()
    
    def _reper(self, no):
        s = ''
        if no is not None:
            s += '%s <- %s -> %s \n' % (no.left and no.left.value, no.value, no.right and no.right.value)
            s += self._reper(no.left)
            s += self._reper(no.right)
        return s

    def represent(self):
        return self._reper(self.raiz)
    
    