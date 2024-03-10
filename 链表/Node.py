class Node(object):
    def __init__(self, elem):
        self.next = None
        self.elem = elem


class single_link_list(object):
    def __init__(self, node):
        if node is not None:
            headNode = Node(node)
            self.__head = headNode
        else:
            self.__head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return: true or false
        """
        return self.__head == None

    def length(self):
        """
        判断链表长度
        :return: int
        """
        cur = self.__head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """
        遍历链表
        :return: void
        """
        cur = self.__head
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """
        在链表头部创建节点（头插）
        :param item: 节点的值
        :return: 一个链表
        """
        cur = Node(item)
        cur.next = self.__head
        self.__head = cur

    def append(self, item):
        """
        在链表尾部创建节点（尾插）
        :param item: 节点的值
        :return: void
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """
        在链表的中间插入一个节点
        :param pos: 节点的位置
        :param item: 节点的值
        :return: void
        """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            count = 0
            pre = self.__head
            while count < pos-1:
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """
        移除链表中是item的节点
        :param item: 节点的值
        :return: 一个链表
        """
        flag = 0
        cur = self.__head
        pre = None
        if cur.elem == item:
            self.__head = cur.next
            flag = 1
        else:
            while cur:
                if cur.elem != item:
                    pre = cur
                    cur = cur.next
                else:
                    pre.next = cur.next
                    flag = 1
                    break
        if flag == 1:
            return True
        else:
            return False

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            cur = cur.next
        return False



if __name__ == '__main__':
    List = single_link_list(0)
    print(List.is_empty())
    print(List.length())
    List.append(1)
    print(List.is_empty())
    print(List.length())
    List.append(2)
    List.append(3)
    List.append(4)
    List.append(5)
    print(List.is_empty())
    print(List.length())
    List.add(10)
    List.insert(2, 100)
    List.insert(-1, 200)
    List.insert(100, 1000)
    List.travel()
    print()
    print(List.remove(200))
    print(List.remove(200))
    List.travel()
    print()
    print(List.search(200))
