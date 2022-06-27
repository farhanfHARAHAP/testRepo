import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(self.root, data)
    
    def insertNode(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insertNode(node.left, data)
        else:
            node.right = self.insertNode(node.right, data)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        return self.settleViolation(node)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def process(self, node):
        print("Tadinya ",node.data," root dari unbalance node")
        while node is not None:
            print(node.data, "Menjadi Kanannya", node.right.data if node.right is not None else "None", "Menjadi Kirinya", node.left.data if node.left is not None else "None")
            node = node.right
             

    def settleViolation(self, node):
        if self.getBalance(node) > 1:
            if self.getBalance(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        elif self.getBalance(node) < -1:
            if self.getBalance(node.right) > 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node


    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

# ALurr
print("\nFarhan Fadillah Harahap - 064002100017\n")

obj = AVL()
lyst = [16, 15, 11, 8, 10, 3, 4, 5, 13]
for i in lyst:
    obj.insert(i)

obj.process(obj.root) 
print("\n[BEFORE] List berdasar modul: \n",lyst)
print("\n[AFTER] PreOrder transversal AVL Tree: ")
obj.preorder(obj.root)

print()
print(50*"=")
    
lyst = []
count = 9
while count != 0:
    cache = random.randint(0, 50)
    if cache in lyst:
        pass
    else:
        lyst.append(cache)
        count -= 1

obj = AVL()
print()    
for i in lyst:
    obj.insert(i)

obj.process(obj.root) 
print("\n[BEFORE] List Random: \n",lyst)
print("\n[AFTER] PreOrder transversal AVL Tree: ")
obj.preorder(obj.root)