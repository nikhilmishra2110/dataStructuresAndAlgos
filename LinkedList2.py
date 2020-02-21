class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insertAtBeginning(self,data):
        tmp = Node(data)
        tmp.next = self.head
        self.head.next = tmp

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            # if key was not present in linked list
        if (temp == None):
            return

            # Unlink the node from linked list
        prev.next = temp.next

        temp = None




if __name__=='__main__':
    ll = LinkedList()
    first = Node(2)
    second = Node(3)
    third = Node(5)

    ll.head = first
    first.next = second
    second.next = third
    ll.printLinkedList()