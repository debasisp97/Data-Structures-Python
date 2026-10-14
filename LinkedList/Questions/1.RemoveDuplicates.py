"""
In a sorted linked list, we need to remove duplicates from linked list
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    temp= linkedList

    while temp is not None:
        curr= temp.next
        while curr is not None and temp.value == curr.value:
            curr=curr.next
        
        temp.next= curr
        temp= temp.next
        
    return linkedList