class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # if head is null
        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        
        # find the max or the last element
        cur = head
        while cur.next!=head and cur.val<=cur.next.val:
            cur = cur.next
        max_node = cur
        
        # print(max_node.val)
        
        # break the circle, create a dummy head
        dummy = Node(-10**6-1, max_node.next)
        max_node.next = None
        
        # insert the value
        cur = dummy
        while cur.next and cur.next.val<=insertVal:
            cur = cur.next
        new_node = Node(insertVal)
        new_node.next = cur.next
        cur.next = new_node
        # 记得maxnode有可能更新的，如果插入值大于maxnode，maxnode要往后移动
        if insertVal>=max_node.val: max_node = new_node
        
        # rebuild the circle
        max_node.next = dummy.next
        return dummy.next