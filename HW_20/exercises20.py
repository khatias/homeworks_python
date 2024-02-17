# 1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList 
#  კლასი რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.
# 2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
# 3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
# 4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove_last(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev is None:
            
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev

    def display(self):
        current = self.head
        while current:
            print(current.value, end="")
            if current.next:
                print(" , ", end="")
            current = current.next
        print()

my_list = LinkedList(5)
my_list.append(10)
my_list.append(15)
my_list.append(20)

my_list.display()

my_list.remove_last()
my_list.display()
