class Queue(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """
        入队
        :param item: int
        :return: void
        """
        self.__list.append(item)

    def pop(self):
        """
        出队
        :return: int
        """
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop(), end=" ")
    print(q.pop(), end=" ")
    print(q.pop(), end=" ")
    print(q.pop(), end=" ")