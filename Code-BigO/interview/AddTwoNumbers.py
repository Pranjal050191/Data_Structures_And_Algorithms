# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1_list = list()
        l1_list_rvrs = list()
        l2_list = list()
        l2_list_rvrs = list()
        l3 = ListNode()
        current = l3
        head = l3
        while(l1):
            l1_list.append(l1.val)
            l1 = l1.next
        while(l2):
            l2_list.append(l2.val)
            l2 = l2.next
        for i in range(len(l1_list)-1,-1,-1):
            l1_list_rvrs.append()
        for i in range(len(l2_list)-1,-1,-1):
            l2_list_rvrs.append()
        x = int(''.join(map(str, l1_list_rvrs)))
        y = int(''.join(map(str, l2_list_rvrs)))
        z = x+y
        z_str = str(z)
        z_str_rvrs = z_str[::-1]
        print(z_str_rvrs)
        # for i in range(len(z_str_rvrs)):
        #     current = dummy.next
        #     current.val = z_str_rvrs[i]
        #     current.next = 


l1 = ListNode()
l1 = [2,4,3]
l2 = [5,6,4]
addTwoNumbers(l1,l2)


        
        
