class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.__size = 1

    def insert(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        if self.tail is not None and self.head is not None:
            self.head = temp
            self.tail.set_next(self.head)
            self.__size += 1
        else:
            self.tail = temp
            self.head = temp

    def size(self):
        return self.__size

    def search(self, data):
        current = self.head
        found = False
        while current.get_data() == data:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def compare(self, two):
        if self.size() != two.size():
            raise ValueError("Different")
        current_one = self.head
        current_two = two.head
        while (current_one != None and current_two != None):
            if (current_one.get_data() != current_two.get_data()):
                raise ValueError("Different")
            current_one = current_one.get_next()
            current_two = current_two.get_next()

    def show(self):
        current = self.head
        while (current != None and current != self.tail):
            print(current.get_data())
            current = current.get_next()
        print(current.get_data())

    def reserve(self):
        current = self.head
        values = []
        while (current):
            values.append(current.get_data())
            current = current.get_next()

        for x in reversed(values):
            print(x)


lista = LinkedList()
lista.insert(1)
lista.insert(2)
lista.insert(3)
lista.show()