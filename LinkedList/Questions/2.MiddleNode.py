"""
Find the middle node of a linked list
"""

# By Length method

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    cnt=0
    temp= linkedList

    while temp is not None:
        cnt+=1
        temp= temp.next

    temp= linkedList
    for _ in range(cnt//2) :
        temp= temp.next
        
    return temp

#########################################
# By Pointers - Slow and Fast pointer
def middleNode(linkedList):
    # Write your code here.
    sp=linkedList
    fp=linkedList

    while fp is not None and fp.next is not None:
        sp=sp.next
        fp= fp.next.next
        
    return sp