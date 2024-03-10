class Node(object):
    def __init__(self, elem):
        self.next = None
        self.elem = elem


class single_cycle_linklist(object):
    def __init__(self):
        self.__head = None

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
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """
        遍历链表
        :return: void
        """
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """
        在链表头部创建节点（头插）
        :param item: 节点的值
        :return: void
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return

        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node

    def append(self, item):
        """
        在链表尾部创建节点（尾插）
        :param item: 节点的值
        :return: void
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            return True
        return False

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
            while count < pos - 1:
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
        if self.is_empty():
            return False
        cur = self.__head
        pre = None
        flag = 0
        # 删除头结点
        if cur.elem == item:
            if cur.next is not self.__head:
                while cur.next is not self.__head:
                    cur = cur.next
                cur.next = self.__head
                self.__head = self.__head.next
            else:
                self.__head = None
                flag = 1
        else:
            pre = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    pre.next = cur.next
                    flag = 1
                else:
                    pre = cur
                    cur = cur.next
            if cur.elem == item:
                flag = 1
                pre.next = cur.next
        if flag==1:
            return True
        else:
            return False

    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next is not self.__head:
                if cur.elem == item:
                    return True
                cur = cur.next
            if cur.elem == item:
                return True
        return False


if __name__ == '__main__':
    List = single_cycle_linklist()
    print(List.is_empty())
    print(List.length())
    List.append(1)
    List.travel()
    print(List.is_empty())
    print(List.length())
    List.append(2)
    List.travel()
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
    print(List.remove(200))
    print(List.remove(200))
    List.travel()
    print(List.search(200))
