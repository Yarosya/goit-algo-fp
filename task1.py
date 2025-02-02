class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def append(self, value):
        new_node = Node(value)
        if not self.head_node:
            self.head_node = new_node
            return
        current_node = self.head_node
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def print_list(self):
        current_node = self.head_node
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def reverse(self):
        previous_node = None
        current_node = self.head_node
        while current_node:
            next_temp = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_temp
        self.head_node = previous_node

    def sorted_merge(self, other_list):
        dummy_head = Node(0)
        tail_pointer = dummy_head
        list_a, list_b = self.head_node, other_list.head_node

        while list_a and list_b:
            if list_a.value <= list_b.value:
                tail_pointer.next_node = list_a
                list_a = list_a.next_node
            else:
                tail_pointer.next_node = list_b
                list_b = list_b.next_node
            tail_pointer = tail_pointer.next_node

        tail_pointer.next_node = list_a if list_a else list_b
        merged_list = SinglyLinkedList()
        merged_list.head_node = dummy_head.next_node
        return merged_list

    def insertion_sort(self):
        sorted_head = None
        current_pointer = self.head_node

        while current_pointer:
            next_temp = current_pointer.next_node
            if not sorted_head or sorted_head.value >= current_pointer.value:
                current_pointer.next_node = sorted_head
                sorted_head = current_pointer
            else:
                temp_pointer = sorted_head
                while temp_pointer.next_node and temp_pointer.next_node.value < current_pointer.value:
                    temp_pointer = temp_pointer.next_node
                current_pointer.next_node = temp_pointer.next_node
                temp_pointer.next_node = current_pointer
            current_pointer = next_temp

        self.head_node = sorted_head

list_one = SinglyLinkedList()
list_one.append(3)
list_one.append(1)
list_one.append(4)
list_one.append(2)

print("Оригінальний список:")
list_one.print_list()

list_one.reverse()
print("Реверсований список:")
list_one.print_list()

list_one.insertion_sort()
print("Відсортований список:")
list_one.print_list()

list_two = SinglyLinkedList()
list_two.append(5)
list_two.append(0)

merged_result_list = list_one.sorted_merge(list_two)
print("Об'єднаний відсортований список:")
merged_result_list.print_list()
