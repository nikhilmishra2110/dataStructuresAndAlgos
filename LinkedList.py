class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        print("Nikhil")
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp=temp.next
    def insertAtBegninning(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert(self, previous_node, data):
        temp = Node(data)

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = temp


    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def searchDataInLL(self, data):
        temp = self.head
        while(temp!=None):
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def detectLoop(self):
        s = set()
        temp = self.head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False


    def detectLoopUsingTwoPointer(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return



if __name__=='__main__':
    llist = LinkedList()
    # Insert 6.  So linked list becomes 6->None
    llist.insertAtBegninning(6)
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.insertAtBegninning(7);
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.insertAtBegninning(1);
     # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.insertAtEnd(4)
     # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insert(llist.head.next, 8)
    print
    'Created linked list is:',
    llist.printList()
    print (llist.head.next)
    print (llist.searchDataInLL(2))
    if llist.searchDataInLL(21):
        print("Yes")

    print (llist.detectLoop())
    # Create a loop for texting
    llist.head.next.next.next.next = llist.head;

    print (llist.detectLoop())
    print (llist.detectLoopUsingTwoPointer())


