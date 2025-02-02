class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.deleted = False  # Lazy deletion flag


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.index_map = {}
        self.next_index = 0 

    def insert(self, i, value):
        new_node = Node(value)

        if i == 0:  # Insert at the head
            new_node.next = self.head
            self.head = new_node
        else:  # Insert at position i
            prev = self.index_map[i - 1] 
            new_node.next = prev.next
            prev.next = new_node

        
        self.index_map[self.next_index] = new_node
        self.next_index += 1
        self.size += 1

    def remove(self, i):
        node = self.index_map[i]
        node.deleted = True 

    def get(self, i):
        node = self.index_map[i]
        while node.deleted:
            i += 1 
            node = self.index_map[i]
        return node.value

    def cleanup(self):
        prev = None
        current = self.head
        new_index_map = {}
        new_index = 0

        while current:
            if current.deleted:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                if not prev:
                    self.head = current
                prev = current
                new_index_map[new_index] = current
                new_index += 1
            current = current.next
        self.index_map = new_index_map
        self.size = new_index

    def printAll(self):
        current = self.head
        i = 0
        while current:
            if not current.deleted:
                print(f"Node {i}: {current.value}", end=" -> ")
                i += 1
            current = current.next
        print("None\n")


def main():
    linkedList = SinglyLinkedList()

    '''Initialize linked list'''
    for i in range(10):
        linkedList.insert(i, i * 100)
    print("Initial linked list")
    linkedList.printAll()

    linkedList.insert(5, "Inserted at 5")
    linkedList.insert(5, "Inserted at 5")
    linkedList.insert(7, "Inserted at 7")
    linkedList.insert(7, "Inserted at 7")
    linkedList.cleanup()
    print("After inserting 4 elements")
    linkedList.printAll()
    print("index 6: ", linkedList.get(6))

   
    linkedList.remove(9)
    linkedList.remove(10)
    linkedList.cleanup()
    print("After deleting 2 elements")
    linkedList.printAll()

    print("index 5: ", linkedList.get(5))


if __name__ == "__main__":
    main()
