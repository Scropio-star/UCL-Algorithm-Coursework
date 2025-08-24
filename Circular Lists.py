class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def isEmpty(self):
        return self.head == None
    def get_length(self):
        return self.length
    def append(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    def prepend(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    def delete_item(self,item):
        current = self.head
        while current.next.item != item:
            current = current.next
        current.next = current.next.next
        self.length -= 1

    def delete_pos(self, pos):
        # 边界条件检查
        if pos < 0 or pos >= self.length:  # 索引范围应为 [0, length-1]
            print("Invalid position")
            return

        if self.head is None:  # 处理空链表
            print("List is empty")
            return

        current = self.head
        if pos == 0:  # 删除头节点
            if self.length == 1:  # 只剩一个节点
                self.head = None
                self.tail = None
            else:
                self.head = current.next  # 更新头节点
                self.tail.next = self.head  # 维护环形：尾节点指向新头节点
        else:  # 删除中间或尾部节点
            prev_node = self.head
            for _ in range(pos - 1):  # 找到待删除节点的前驱节点
                prev_node = prev_node.next
            node_to_delete = prev_node.next
            prev_node.next = node_to_delete.next  # 跳过待删除节点

            if node_to_delete == self.tail:  # 若删除尾节点，更新尾指针
                self.tail = prev_node
        self.size -= 1
    def access(self,pos):
        if pos < 0 or pos >= self.length:
            print("Invalid position")
            return
        if self.head is None:  # 处理空链表
             print("List is empty")
             return
        if pos == 0:
            print(self.head.item)
        else:
            current = self.head
            for _ in range(pos):# 找到目标节点
                current = current.next
            print(current.item)
if __name__ == '__main__':
    # 创建链表实例
    ll = CircularList()

    # 插入一些元素
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print(ll.length)
    # 测试 access 方法
    print("访问位置 0:")
    ll.access(0)  # 应该输出 10

    print("访问位置 1:")
    ll.access(1)  # 应该输出 20

    print("访问位置 2:")
    ll.access(2)  # 应该输出 30

    print("访问位置 4 (无效):")
    ll.access(4)  # 应该输出 "Invalid position"
    #



