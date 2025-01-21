class Node: 

    def __init__(self, data): 

        self.data = data 

        self.next = None 

        self.position = None 

        pass 

 

#incomplete 

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

    linkedList = {} 

    head = Node(0) 

    for i in range(20): 

        linkedList[i] = insert_at_end(head, i * 2) 

 

    insert(head, linkedList, 21, 1) 

# print(get(linkedList, 21).data) 

    return 0 

 

if __name__ == "__main__": 

    main() 