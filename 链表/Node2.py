# 定义节点
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 构造单向链表
class SingleLinkedList:
    # 判断链表是否为空：_head指向None，则为空
    def is_empty(self):
        '''
        if self._head==None:
            print("True")
        else:
            print("False")
            '''
        return self._head == None

    # 单向链表初始化
    def __init__(self, node=None):
        # 判断node是否为空
        if node != None:
            headNode = Node(node)
            self._head = headNode
        else:
            self._head = node

    # 计算链表长度
    def length(self):
        count = 0
        curNode = self._head
        while curNode != None:
            count += 1
            curNode = curNode.next
            return count

    # 遍历链表
    def travel(self):
        curNode = self._head
        while curNode != None:
            print(curNode.elem, end='\t')
            curNode = curNode.next
        print("  ")

    # 在头部添加元素
    def add(self, item):
        # 将传入的值构造成节点
        node = Node(item)
        # 将新节点的链接域next指向头节点
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    # 在尾部添加元素
    def append(self, item):
        # 将传入的值构造成节点
        node = Node(item)
        if self.is_empty():  # 单链表为空
            self._head = node
        else:  # 单链表不为空
            curNode = self._head
            while curNode.next != None:
                curNode = curNode.next
            # 修改节点，最后一个节点的next指向node
            curNode.next = node

    # 在指定位置添加元素
    def insert(self, pos, item):
        # 如果pos<=0，默认插入到头部
        if pos <= 0:
            self.add(item)
        # 如果pos>链表长度，直接在尾部追加
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 构造节点
            node = Node(item)
            count = 0
            preNode = self._head
            while count < (pos - 1):  # 查找前一个节点
                count += 1
                preNode = preNode.next
            # 修改指向
            # 将前一个节点的next指向插入节点
            node.next = preNode.next
            # 将插入位置的前一个节点next指向新节点
            preNode.next = node

    # 查找节点是否存在
    def search(self, item):
        curNode = self._head
        while curNode != None:
            if curNode.elem == item:
                return True
            curNode = curNode.next
        return False

    # 删除节点
    def remove(self, item):
        curNode = self._head
        preNode = None
        while curNode != None:
            if curNode.elem == item:
                # 判断是否是头节点
                if preNode == None:  # 是头节点
                    self._head = curNode.next
                else:
                    # 删除
                    preNode.next = curNode.next
            break
        else:
            preNode = curNode
            curNode = curNode.next


if __name__ == "__main__":
    # 初始化元素值为10单向链表
    singleLinkedList = SingleLinkedList(30)
    print("是否为空链表：", singleLinkedList.is_empty())
    print("链表长度为：", singleLinkedList.length())
    print("----遍历链表----")
    singleLinkedList.travel()
    print("-----查找-----", singleLinkedList.search(30))
    print("-----头部插入-----")
    singleLinkedList.add(1)
    singleLinkedList.add(2)
    singleLinkedList.add(3)
    singleLinkedList.travel()
    print("-----尾部追加-----")
    singleLinkedList.append(10)
    singleLinkedList.append(20)
    singleLinkedList.travel()
    print("-----链表长度-----", singleLinkedList.length())
    print("-----指定位置插入-----")
    singleLinkedList.insert(-1, 100)
    singleLinkedList.travel()
    print("-----删除节点-----")
    singleLinkedList.remove(100)
    singleLinkedList.travel()