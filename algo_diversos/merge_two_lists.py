class ListNode(object):
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

    def __repr__(self):
        return str(self.value)


def mergeTwoLists(l1, l2):
    if l1 is None and l2 is None:
        return None

    head1 = l2[0]
    head2 = l1[0]
    result = []
    while head1.next is not None and head2.next is not None:
        if head1.val <= head2.val:
            result.append(head1)
            head1 = head1.next
        elif head2.val < head1.val:
            result.append(head2)
            head2 = head2.next

    return result



if __name__ == '__main__':

    list1 = []
    a1 = ListNode(1)
    list1.append(a1)
    a2 = ListNode(2)
    a1.next = a2
    list1.append(a2)
    a3 = ListNode(4)
    a2.next = a3
    list1.append(a3)
    list2 = []
    b1 = ListNode(1)
    list1.append(b1)
    b2 = ListNode(3)
    b1.next = b2
    list1.append(b2)
    b3 = ListNode(4)
    b2.next = b3
    list1.append(b3)

    print(mergeTwoLists(list1, list2))