'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sumList = []
        while l1 != None or l2 != None:
            n1 = l1.val if l1 != None else 0
            n2 = l2.val if l2 != None else 0
            sumList.append(n1 + n2)

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        print(sumList)

        flag = 0
        result = None
        for num in sumList:
            if result == None:
                result = ListNode((num + flag) % 10)
            else:
                result.next = ListNode((num + flag) % 10)
            flag = (num + flag) // 10
            result = result.next
            
            
        return None


l1 = ListNode(2, ListNode(4, ListNode(8)))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(8, ListNode(6)))))
s1 = Solution()
s1.addTwoNumbers(l1, l2)

        
            
