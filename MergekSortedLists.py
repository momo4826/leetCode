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
        n = ListNode(0)
        answer = n
        v = []
        for item in lists:
            while item:
                v.append(item.val)
                item = item.next
        v.sort()
        for val in v:
            n.next = ListNode(val)
            n = n.next
        return answer.next
        
#divide and conquer
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
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        l = self.mergeKLists(lists[0:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
        
        
    
    def merge(self, l, r):
        res = ListNode(0)
        answer = res
        while l and r:
            if l.val < r.val:
                res.next = ListNode(l.val)
                l = l.next
            else:
                res.next = ListNode(r.val)
                r = r.next
            res = res.next
        res.next = l or r
        return answer.next
