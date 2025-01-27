class Node: 

    def __init__(self, data): 

        self.data = data 

        self.next = None 

        self.position = None 

        pass 

 

#incomplete 
class LinkedList:
    def __init__(self):
        self.head = None  
        self.hash = {}
        self.length = 0
        

    def insert(self, position, data):

        new_node = Node(data)

        if not self.head:  
            self.head = new_node
            self.hash[0] = new_node
            self.length += 1
            return

        if position > self.length: 

            print("Error out of bounds") 

            return None 


        if self.hash[position-1]:
            prev_node = self.hash[position - 1]
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1


            for i in range(self.length - 1, position, -1):
                self.hash[i] = self.hash[i - 1]
            self.hash[position] = new_node
            return
            



    def display(self):
        """Display all the elements in the linked list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def insert(head, linkedList, position, data): 

    newNode = Node(data) 

#check position. eg: if linked list has 20 elements, position = 25 returns error 

    if position > len(linkedList): 

        print("Error") 

        return None 

    if position == 0: 

    #insert front of linked list 

        newNode.next = head 

        head = newNode 

    else: 

        prev = linkedList[position - 1] 

        prev.next = newNode 

        linkedList[position] = newNode 

    #Still need to shift other nodes 1 over 

 

    return 

 

# O(n) time complexity 

def insert_at_end(head, data): 

    newNode = Node(data) 

    curr = head 

    while curr.next != None: 

        curr = curr.next 

        curr.next = newNode 

        curr = newNode 

        # print(curr.data) 

        return curr 

 

# Need to get previous node, get next node, change prev node.next = curr node.nex 

def remove(linkedList, position): 

    node = linkedList[position] 

    prev = linkedList[position - 1] 

    next = linkedList[position + 1] 

    return 

 

# Takes position as variable, return linked list item O(1) 

def get(linkedList, position): 

    if position > len(linkedList): 

        print("Error") 

        return None 

    return linkedList[position] 

 

def main(): 

 

# Creates linked list with 20 elements 

    linkedlist = LinkedList()

    # linked list initialisation
    linkedlist.insert(0, 111)
    linkedlist.insert(1, 123)
    for i in range(2, 10):
        linkedlist.insert(i, i*2)

    linkedlist.insert(4, 69) # test insertion in the middle

    linkedlist.insert(50, 888) # out of bounds insertion

    linkedlist.display()
    print(linkedlist.hash)

    # linkedList = {} 

    # head = Node(0) 

    # for i in range(20): 

    #     linkedList[i] = insert_at_end(head, i * 2) 

    # insert(head, linkedList, 21, 1) 

# print(get(linkedList, 21).data) 


    return 0 

 

if __name__ == "__main__": 

    main() 