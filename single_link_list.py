class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class Link_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self,newnode):
        if self.head == None:
            self.head = newnode
            self.size += 1
        else:
            last_node = self.head
            while True:
                if last_node.pointer == None:
                    break
                last_node = last_node.pointer
            last_node.pointer = newnode
            self.size += 1

    def print_linklist(self):
        if self.head == None:
            print("List is Empty")
            return
        else:
            last_node = self.head
            while True:
                print(last_node.data)
                if last_node.pointer == None:
                    break
                last_node = last_node.pointer

    def insert_node_start(self,newnode):
        if self.head == None:
            self.head = newnode
            self.size +=1
        else:
            current_head = self.head
            self.head = newnode
            newnode.pointer = current_head
            self.size += 1

    def insertAt(self,newnode,position):
        if position >= self.size:
            print("Out Of Range")
        else:
            current_node = self.head
            current_position = 0
            while True:
                if current_position == position:
                    prenode.pointer = newnode
                    newnode.pointer = current_node
                    break
                prenode = current_node
                current_position+=1
                current_node = current_node.pointer

    def remove_mode(self,position):
        if position >= self.size:
            print("Node out of bound")
            return
        else:
            current_node = self.head
            current_position = 0
            while True:
                if current_position == position:
                    pre_node.pointer = current_node.pointer
                    # del(current_node)
                    return
                pre_node = current_node
                current_node=current_node.pointer
                current_position = current_position+1

    def remove_node_end(self):
        current_node = self.head
        while True:
            if current_node.pointer is None:
                pre_node.pointer = None
                return
            pre_node = current_node
            current_node = current_node.pointer

    def remove_node_start(self):
        self.head = self.head.pointer
        return

    def reverse_linklist(self):
        pre_node = None
        current_node = self.head

        while current_node is not None:
            temp = current_node
            current_node = current_node.pointer
            temp.pointer = pre_node
            pre_node = temp

        self.head = pre_node

    def searching(self,data):
        last_node = self.head
        position = 0
        while last_node is not None:
            print(position)
            print (type(last_node.data))
            print(type(data))
            if last_node.data == data:
                return position
            last_node = last_node.pointer
            position = position+1


node1 = Node(8)
node2 = Node(9)
node3 = Node(10)
node4 = Node(7)
node6 = Node(15)
node5 = Node(16)
link_list = Link_list()
link_list.insert_node(node1)
link_list.insert_node(node2)
link_list.insert_node(node3)
link_list.insert_node_start(node4)
link_list.insert_node_start(node6)
link_list.insertAt(node5,2)
# link_list.remove_mode(3)
# link_list.remove_node_end()
# link_list.remove_node_start()

link_list.print_linklist()

print("-------------")
# link_list.reverse_linklist()
# link_list.print_linklist()
print(link_list.searching(10))


