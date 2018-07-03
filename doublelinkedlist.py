class Node():
    def __init__(self, next_node=None, prev_node=None, data=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = data

    def set_data(self,da):
        self.data = da

class LinkedList():
    def __init__(self, node):
        self.first_node = node
        self.last_node = node
        self.size = 1

    def push(self,node):
        node.next_node = self.first_node
        node.prev_node = self.last_node
        self.last_node.next_node = node
        self.first_node.prev_node = node
        self.first_node = node
        self.size += 1


    def pop(self):
        old_last_node = self.last_node
        to_be_last = self.last_node.prev_node
        to_be_last.next_node = self.first_node
        self.first_node.prev_node = to_be_last
        del old_last_node
        self.last_node = to_be_last
        size -= 1

    def insert(self,node,pos):
        cont = 1
        next = self.first_node
        if (pos == 1):
            self.push()
        else:
            while cont < pos-1:
                next = next.next_node
                cont += 1
            next.next_node = node
            node.prev_node = next
            self.size += 1

    def remove(self,node):
        next_node = node.next_node
        prev_node = node.prev_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
        node.next_node = node.prev_node = None
        return node

    def __str__(self):
        next_node = self.first_node
        s = ""
        while next_node:
            s += "({:0>2d})\n".format(next_node.data)
            next_node = next_node.next_node
        return s

    def maior(self):
        next = self.first_node
        maior = 0
        while next:
            if(maior < next.data):
                maior = next.data
            next = next.next_node
        return maior

    def menor(self):
        next = self.first_node
        menor = next.data
        while next:
            if(menor > next.data):
                menor = next.data
            next = next.next_node
        return menor

    def media(self):
        next = self.first_node
        cont = 0
        sum = 0
        while next:
            sum += next.data
            cont += 1
            next = next.next_node
        media = sum/cont
        return media

    def troca(self,old,new):
        next = self.first_node
        while next:
            if (next.data == old):
                next.set_data(new)
            next = next.next_node




node1 = Node(data=1)
node2 = Node(data=2)
node3 = Node(data=3)
node4 = Node(data=4)
lista = LinkedList(node1)
lista.insert(node2,2)
lista.insert(node3,3)

lista.troca(4,1)
print (lista)
