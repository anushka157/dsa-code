#Problem: Reverse Nodes in k-Group (Linked List)
#Description

#Given a linked list, reverse the nodes of the list k at a time and return the modified list.

#If the number of nodes is not a multiple of k, leave the remaining nodes as-is.

#Medium difficulty because it combines linked list manipulation and iterative logic

#Common in linked list coding interviews





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse(start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    node = head
    count = 0
    while node and count != k:
        node = node.next
        count += 1
    if count == k:
        reversed_head = reverse(head, node)
        head.next = reverseKGroup(node, k)
        return reversed_head
    return head

# ---------------- Example Usage ----------------
def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

if __name__ == "__main__":
    # create linked list 1->2->3->4->5
    nodes = [ListNode(i) for i in range(1,6)]
    for i in range(4):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    k = 2
    new_head = reverseKGroup(head, k)
    print_list(new_head)
