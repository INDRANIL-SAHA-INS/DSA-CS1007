class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLinkedList():
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head==None:
            new_node.next=new_node
            self.head=new_node
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next

            current.next=new_node
            new_node.next=self.head
            
    def delete_node(self):
        if self.head==None:
            print("circular list empty")
            return
        if self.head.next==self.head:
            print(self.head.data," deleted ")
            self.head=None
            return

        current=self.head
        while current.next!=self.head:
            current=current.next

        temp=self.head
        current.next=self.head.next
        self.head=self.head.next
        temp=None
    def display(self):
        if self.head==None:
            print("circular list empty")
            return
        current=self.head
        while True:
            print(current.data,end="--->")
            current=current.next
            if current==self.head:
                break




cll=CircularLinkedList()
cll.insert_at_begining(12)
cll.insert_at_begining(2)
cll.insert_at_begining(10)
cll.insert_at_begining(8)
cll.insert_at_begining(3)
cll.insert_at_begining(11)
cll.insert_at_begining(90)
cll.display()
cll.delete_node()
cll.delete_node()
print()
cll.display()