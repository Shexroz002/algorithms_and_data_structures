"""
Linked Lists ware created in here by Shehrozbek.
26.09.2022
"""

class Node:
    """ Node (Tugun) object"""
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self,prev_data,new_data):
        new_node = Node(new_data)
        new_node.next = prev_data.next
        prev_data.next = new_node
    
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def delete_node(self,key,new_info):
        temp = self.head
        """ check is first node which isn't None """
        if(temp and temp.data == key):
            self.head = temp.data
            temp = None
            return
        """ Look for item which is necessatry  """
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        """  if item was not found """
        if prev is None:
            return
        """ if item was found """
        prev.next = temp.next
        """ node will be deleted """
        temp = None
    
    def update_node_data(self,key,new_info):
        temp = self.head
        """ check is first node which isn't None """
        if(temp and temp.data == key):
            self.head = temp.data
            temp = None
            return
        """ Look for item which is necessatry  """
        while temp:
            if temp.data == key:
                break
            temp = temp.next
        """ if item  find,node will be updated """
        temp.data = new_info
            


    
    


linked_list = LinkedList()
monday = Node('Monday')
thusday = Node('Thusday')
wednisday = Node('wedinsday')
monday.next = thusday
thusday.next = wednisday
linked_list.head = monday
linked_list.push('Monday Morning')
linked_list.append('monday afternoon')
linked_list.update_node_data('Monday','Salom')
linked_list.print_list()

