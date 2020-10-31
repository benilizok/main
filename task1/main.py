
class HashTable:

    def __init__(self, mod):
        self.values = []
        self.values.append(SinglyLinkedList())
        self.values[0].insert(0)
        self.mod = mod
        self.size = 1

    # Insert new element to HashTable
    def insert(self, new_value):
        m = new_value % self.mod
        if m < self.size:
            self.values[m].insert(new_value)
        else:
            i = 1
            while i != m:
                self.values.append(SinglyLinkedList())
                self.values[i].insert(i)
                self.size = self.size + 1
                i = i + 1
            self.values.append(SinglyLinkedList())
            self.values[m].insert(m)
            self.size = self.size + 1
            self.values[m].insert(new_value)

    # Output the HashTable
    def show(self):
        for i in range(self.size):
            self.values[i].iterate()
            print()


class ListNode:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    # Insert at the end of the list
    def insert(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = new_node

    # Output the SingleLinkedList
    def iterate(self):
        node = self.head
        while node:
            if node == self.head:
                print(node.data, ': ', end='')
                node = node.next_node
            else:
                print(node.data, ' ', end='')
                node = node.next_node


if __name__ == '__main__':
    my_hash_table = HashTable(int(input()))
    data_str = input().split()
    i = 0
    while i < len(data_str):
        my_hash_table.insert(int(data_str[i]))
        i += 1
    my_hash_table.show()
