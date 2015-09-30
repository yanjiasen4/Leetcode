# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        listval = [];
        for node in lists:
            while node:
                listval.append(node.val)
                node = node.next
        
        listval.sort()
        if not listval: return []
        result = res_pointer = ListNode(listval[0])
        for i in listval[1:]:
            res_pointer.next = ListNode(i)
            res_pointer = res_pointer.next
        return result