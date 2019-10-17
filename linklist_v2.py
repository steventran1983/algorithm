class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Link_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self,new_node):
        if self.head == None:
            self.head = new_node
            self.size +=1
        else:
            current_head = self.head
            self.head = new_node
            new_node.next = current_head
            self.size += 1

    def insert_end(self,new_node):
        if self.head is None:
            self.head = new_node
            self.size +=1
        else:
            current_head = self.head
            while True:
                if current_head.next is None:
                    current_head.next = new_node
                    break
                current_head = current_head.next
            self.size += 1

    def print_list(self):
        if self.head is None:
            print("List is Empty")
            exit()
        else:
            current_node = self.head
            while True:
                print(current_node.data)
                if current_node.next is None:
                    break
                current_node = current_node.next

    def insertAt(self,newnode,position):
        if position >= self.size:
            print("Out Of Range")
        else:
            current_node = self.head
            current_position = 0
            while True:
                # if current_position == position:
                #     newnode.next = current_node.next
                #     current_node.next = newnode
                current_node = current_node.next
                current_position += 1

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

link_list = Link_list()
link_list.insert_end(node1)
link_list.insert_end(node2)
link_list.insert_end(node3)
link_list.insert_end(node4)
print(link_list.print_list())
print(link_list.size)
link_list.insertAt(node5,2)